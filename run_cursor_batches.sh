#!/usr/bin/env bash

set -euo pipefail
IFS=$'\n\t'

# Configuration with sensible defaults
ERRORS_FILE=${1:-/home/ubuntu/spack-repo/errors.txt}
BATCH_SIZE=${2:-1} # 1 package per batch
SLEEP_SECONDS=${3:-300} # 5 minutes

# Resolve absolute path for logs base
LOG_BASE_DIR=${LOG_BASE_DIR:-/home/ubuntu/spack-repo/cursor_logs}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_DIR="$LOG_BASE_DIR/$TIMESTAMP"
mkdir -p "$LOG_DIR"

# Basic checks
if [[ -z "${DRY_RUN:-}" ]] && ! command -v cursor-agent >/dev/null 2>&1; then
  echo "Error: cursor-agent is not found in PATH." >&2
  exit 1
fi

if [[ ! -f "$ERRORS_FILE" ]]; then
  echo "Error: errors file not found at: $ERRORS_FILE" >&2
  exit 1
fi

# Read non-empty, non-comment lines
mapfile -t RAW_LINES < <(sed -e 's/\r$//' "$ERRORS_FILE")
LINES=()
for line in "${RAW_LINES[@]}"; do
  # Trim leading/trailing whitespace using sed (portable)
  trimmed=$(echo -n "$line" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
  # Skip empty and comment lines
  if [[ -z "$trimmed" ]] || [[ "$trimmed" =~ ^# ]]; then
    continue
  fi
  LINES+=("$trimmed")
done

TOTAL=${#LINES[@]}
if (( TOTAL == 0 )); then
  echo "No tasks found in $ERRORS_FILE" >&2
  exit 0
fi

echo "Found $TOTAL tasks in $ERRORS_FILE. Launching in batches of $BATCH_SIZE every $SLEEP_SECONDS seconds." >&2
echo "Logs: $LOG_DIR" >&2
if [[ -n "${DRY_RUN:-}" ]]; then
  echo "DRY_RUN is set: will print commands instead of executing them." >&2
fi

index=0
batch_number=0
while (( index < TOTAL )); do
  ((++batch_number))
  echo "Starting batch #$batch_number at $(date -Is)" >&2

  # Determine how many to launch in this batch
  remaining=$(( TOTAL - index ))
  launch_count=$(( remaining < BATCH_SIZE ? remaining : BATCH_SIZE ))

  for (( i=0; i<launch_count; i++ )); do
    pkg="${LINES[index+i]}"
    safe_pkg_filename=$(echo "$pkg" | tr '/ :@' '____')
    log_out="$LOG_DIR/${batch_number}_${i+1}_${safe_pkg_filename}.out.log"
    log_err="$LOG_DIR/${batch_number}_${i+1}_${safe_pkg_filename}.err.log"

    echo "  Launching: $pkg (logs: $(basename "$log_out"), $(basename "$log_err"))" >&2
    if [[ -n "${DRY_RUN:-}" ]]; then
      echo "    cmd: cursor-agent -p \"try installing ${pkg} and debug the errors\" --model \"gpt-5\" " >&2
    else
      nohup bash -c \
        "cursor-agent -p \"try installing and validating ${pkg} and debug the errors iteratively, until it succeeds. Do not give up.\" --model \"gpt-5\" --output-format text" \
        >"$log_out" 2>"$log_err" &
    fi
  done

  index=$(( index + launch_count ))

  # If there are more lines to process, sleep before next batch
  if (( index < TOTAL )); then
    echo "Batch #$batch_number launched. Sleeping for $SLEEP_SECONDS seconds before next batch..." >&2
    sleep "$SLEEP_SECONDS"
  fi
done

echo "All $TOTAL tasks have been launched. Exiting at $(date -Is)." >&2

