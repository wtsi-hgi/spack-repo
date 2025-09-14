#!/usr/bin/env bash

set -euo pipefail

# Configuration
ROOT_DIR="/home/ubuntu/spack-repo"
LOG_DIR="$ROOT_DIR/install_logs"
OUTPUT_JSON="$LOG_DIR/failure-reasons.json"

# Directory to store streamed Codex agent logs and last messages
STREAM_LOG_DIR="$LOG_DIR/codex-failure-reason-sessions"


if [[ ! -d "$LOG_DIR" ]]; then
  echo "Logs directory not found: $LOG_DIR" >&2
  exit 1
fi

have_jq=1
if ! command -v jq >/dev/null 2>&1; then
  have_jq=0
  echo "Warning: jq not found. Will build JSON array without jq." >&2
fi
if ! command -v codex >/dev/null 2>&1; then
  echo "codex CLI not found in PATH" >&2
  exit 1
fi

trim_to_bytes() {
  # Trim stdin to given number of bytes
  local limit_bytes="$1"
  # Use dd to enforce byte limit without breaking on long lines
  dd bs=1 count="$limit_bytes" 2>/dev/null || true
}

# find_latest_log_for_pkg is no longer needed when iterating logs directly

extract_error_excerpt() {
  local log_file="$1"
  local max_bytes=16000
  # Prefer focused excerpt around the last error-like line
  local last_err_line
  last_err_line=$(grep -inE '(error|failed|exception|traceback|fatal|cmake error|ld: error|undefined reference|no such file|could not find|conflict|resolution failed)' "$log_file" | tail -n1 | cut -d: -f1 || true)
  if [[ -n "$last_err_line" ]]; then
    local start_line end_line
    start_line=$(( last_err_line - 60 ))
    end_line=$(( last_err_line + 60 ))
    if (( start_line < 1 )); then start_line=1; fi
    awk -v s="$start_line" -v e="$end_line" 'NR>=s && NR<=e' "$log_file" | trim_to_bytes "$max_bytes"
    return 0
  fi
  # Fallback to tail if no clear error lines
  tail -n 400 "$log_file" | trim_to_bytes "$max_bytes"
}

summarize_with_codex() {
  local pkg="$1"
  local excerpt_file="$2"
  local log_label="${3:-}"

  local tmp_prompt tmp_last
  tmp_prompt=$(mktemp)
  # Per-package session artifacts
  local pkg_safe ts session_log
  pkg_safe=$(echo "$pkg" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9._-]+/-/g; s/^-+//; s/-+$//')
  ts=$(date +%s)
  session_log="$STREAM_LOG_DIR/${pkg_safe}-${ts}.txt"
  tmp_last="$STREAM_LOG_DIR/${pkg_safe}-${ts}.last.json"

  {
    printf '\nPackage: %s\n' "$pkg"
    if [[ -n "$log_label" ]]; then
      printf 'Log file: %s\n' "$log_label"
    fi
    printf '\nInstall log excerpt path: "%s"' "$excerpt_file"
    printf '\n\nFollow the schema in /home/ubuntu/spack-repo/AGENTS.md. Output strict JSON with keys "package" and "failure_reason", and optionally "lowest_r_version" if R version constraints are implicated. No other text.\n'
  } >> "$tmp_prompt"

  # Run codex non-interactively; stream JSONL events to session_log and capture last message
  if ! codex exec --sandbox danger-full-access --output-last-message "$tmp_last" - < "$tmp_prompt" 2>&1 | tee "$session_log" >/dev/null; then
    rm -f "$tmp_prompt"
    return 1
  fi

  local content
  content=$(cat "$tmp_last" 2>/dev/null || true)
  rm -f "$tmp_prompt"

  if [[ -z "$content" ]]; then
    return 1
  fi

  # Ensure JSON
  if ! printf '%s' "$content" | jq -e . >/dev/null 2>&1; then
    local fragment
    fragment=$(printf '%s' "$content" | sed -n '1h;1!H;${;g;s/^[^{]*//;s/[^}]*$//;p;}')
    if [[ -n "$fragment" ]] && printf '%s' "$fragment" | jq -e . >/dev/null 2>&1; then
      content="$fragment"
    else
      return 1
    fi
  fi

  printf '%s' "$content"
  return 0
}

main() {
  local tmp_results
  tmp_results=$(mktemp)
  : >"$tmp_results"

  mkdir -p "$STREAM_LOG_DIR"

  shopt -s nullglob
  local log_files=("$LOG_DIR"/*.log)
  shopt -u nullglob

  if (( ${#log_files[@]} == 0 )); then
    echo "No .log files found in: $LOG_DIR" >&2
    rm -f "$tmp_results"
    exit 1
  fi

  for log_file in "${log_files[@]}"; do
    # Only process logs that appear to contain errors
    if ! grep -qiE '(error|failed|exception|traceback|fatal|cmake error|ld: error|undefined reference|no such file|could not find|conflict|resolution failed)' "$log_file" 2>/dev/null; then
      continue
    fi

    local log_base
    log_base="$(basename -- "$log_file")"
    local name_no_ext package_name
    name_no_ext="${log_base%.log}"
    package_name=$(printf '%s' "$name_no_ext" | sed -E 's/-[0-9]+(\.[0-9]+)*$//')

    # Extract error-focused excerpt to a temp file
    local tmp_excerpt
    tmp_excerpt=$(mktemp)
    extract_error_excerpt "$log_file" > "$tmp_excerpt"

    # Codex summarization (no fallback)
    local json_out
    if json_out=$(summarize_with_codex "$package_name" "$tmp_excerpt" "$log_base" 2>/dev/null); then
      if (( have_jq == 1 )); then
        printf '%s' "$json_out" | jq --arg pkg "$package_name" 'if (has("package") and (.package|type=="string") and (.package|length>0)) then . else . + {package:$pkg} end' >>"$tmp_results"
        printf '\n' >>"$tmp_results"
      else
        printf '%s\n' "$json_out" >>"$tmp_results"
      fi
    else
      if (( have_jq == 1 )); then
        jq -n --arg package "$package_name" --arg failure_reason "Summarization failed" '{package:$package, failure_reason:$failure_reason}' >>"$tmp_results"
      else
        printf '{"package":"%s","failure_reason":"Summarization failed"}\n' "$package_name" >>"$tmp_results"
      fi
    fi
    rm -f "$tmp_excerpt"
  done

  # Combine results into a JSON array
  if (( have_jq == 1 )); then
    jq -s '.' "$tmp_results" >"$OUTPUT_JSON"
  else
    # Best-effort wrap into array separated by commas
    {
      printf '['
      paste -sd',' "$tmp_results"
      printf ']'
    } >"$OUTPUT_JSON"
  fi

  rm -f "$tmp_results"
  echo "Wrote: $OUTPUT_JSON"
}

main "$@"

