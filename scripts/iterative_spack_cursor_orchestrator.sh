#!/usr/bin/env bash

set -euo pipefail
IFS=$'\n\t'

# Defaults (can be overridden by flags)
ERRORS_FILE="/home/ubuntu/spack-repo/errors.txt"
BATCH_SIZE=1
SLEEP_SECONDS=300         # delay between launches inside run_cursor_batches
MAX_ROUNDS=10

SCRIPT_DIR="/home/ubuntu/spack-repo/scripts"
RUN_BATCHES_SH="/home/ubuntu/spack-repo/scripts/run_cursor_batches.sh"
CHECK_SCRIPT="$SCRIPT_DIR/check_spack_installed.sh"
OUT_BASE="/home/ubuntu/spack-repo/iterative_runs"

print_usage() {
  cat <<EOF
Usage: $(basename "$0") [options]

Options:
  --errors FILE           Path to initial errors file (default: $ERRORS_FILE)
  --batch-size N          Batch size per run (default: $BATCH_SIZE)
  --sleep-seconds S       Sleep between launches inside a run (default: $SLEEP_SECONDS)
  --max-rounds N          Maximum number of iterations (default: $MAX_ROUNDS)
  --dry-run               Set DRY_RUN for run_cursor_batches (no jobs launched)
  -h, --help              Show this help

This orchestrates iterative runs of run_cursor_batches and filters the failing
packages after each round using check_spack_installed.sh, until no progress or
no failures remain. Outputs are saved under $OUT_BASE/<timestamp>/
EOF
}

DRY_RUN_FLAG=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --errors)
      ERRORS_FILE="$2"; shift 2;;
    --batch-size)
      BATCH_SIZE="$2"; shift 2;;
    --sleep-seconds)
      SLEEP_SECONDS="$2"; shift 2;;
    --max-rounds)
      MAX_ROUNDS="$2"; shift 2;;
    --dry-run)
      DRY_RUN_FLAG="1"; shift 1;;
    -h|--help)
      print_usage; exit 0;;
    *)
      echo "Unknown argument: $1" >&2; print_usage; exit 1;;
  esac
done

# Checks
command -v jq >/dev/null 2>&1 || { echo "Error: jq is required" >&2; exit 1; }
[[ -x "$RUN_BATCHES_SH" ]] || { echo "Error: $RUN_BATCHES_SH not executable" >&2; exit 1; }
[[ -x "$CHECK_SCRIPT" ]] || { echo "Error: $CHECK_SCRIPT not executable" >&2; exit 1; }
[[ -f "$ERRORS_FILE" ]] || { echo "Error: errors file not found: $ERRORS_FILE" >&2; exit 1; }

timestamp=$(date +%Y%m%d_%H%M%S)
RUN_DIR="$OUT_BASE/$timestamp"
mkdir -p "$RUN_DIR"

echo "Starting iterative orchestration at $(date -Is)" | tee "$RUN_DIR/summary.log"
echo "Inputs: errors=$ERRORS_FILE batch_size=$BATCH_SIZE sleep_seconds=$SLEEP_SECONDS max_rounds=$MAX_ROUNDS dry_run=${DRY_RUN_FLAG:+yes}" | tee -a "$RUN_DIR/summary.log"

prev_errors="$ERRORS_FILE"
prev_count=$(grep -vE '^\s*#' "$prev_errors" | sed -e 's/\r$//' | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' | grep -vE '^\s*$' | wc -l | awk '{print $1}')

for (( round=1; round<=MAX_ROUNDS; round++ )); do
  echo "\n=== Round $round | $(date -Is) ===" | tee -a "$RUN_DIR/summary.log"
  round_dir="$RUN_DIR/round-$round"
  mkdir -p "$round_dir"

  echo "Launching run_cursor_batches on $prev_errors (count=$prev_count)" | tee -a "$RUN_DIR/summary.log"
  if [[ -n "$DRY_RUN_FLAG" ]]; then
    DRY_RUN=1 "$RUN_BATCHES_SH" "$prev_errors" "$BATCH_SIZE" "$SLEEP_SECONDS" | tee "$round_dir/run_cursor_batches.dry.log"
  else
    "$RUN_BATCHES_SH" "$prev_errors" "$BATCH_SIZE" "$SLEEP_SECONDS" | tee "$round_dir/run_cursor_batches.log"
  fi


  report_json="$round_dir/report.json"
  echo "Checking installed status for this round's list..." | tee -a "$RUN_DIR/summary.log"
  "$CHECK_SCRIPT" "$prev_errors" > "$report_json"

  # Create next errors file from failing ones
  next_errors="$round_dir/errors-next.txt"
  jq -r '.results[] | select(.installed==false) | .raw' "$report_json" > "$next_errors"
  next_count=$(wc -l "$next_errors" | awk '{print $1}')

  success_count=$(jq '[.results[] | select(.installed)] | length' "$report_json")
  echo "Round $round: success=$success_count, remaining_failures=$next_count (was $prev_count)" | tee -a "$RUN_DIR/summary.log"

  # Stop conditions
  if (( next_count == 0 )); then
    echo "All packages succeeded by round $round." | tee -a "$RUN_DIR/summary.log"
    ln -sf "$(realpath -e "$next_errors")" "$RUN_DIR/final_errors.txt" || true
    ln -sf "$(realpath -e "$report_json")" "$RUN_DIR/final_report.json" || true
    break
  fi

  if (( next_count >= prev_count )); then
    echo "No further progress (remaining $next_count, previous $prev_count). Stopping." | tee -a "$RUN_DIR/summary.log"
    ln -sf "$(realpath -e "$next_errors")" "$RUN_DIR/final_errors.txt" || true
    ln -sf "$(realpath -e "$report_json")" "$RUN_DIR/final_report.json" || true
    break
  fi

  # Prepare next round
  prev_errors="$next_errors"
  prev_count="$next_count"
done

echo "Outputs directory: $RUN_DIR" | tee -a "$RUN_DIR/summary.log"
echo "Done at $(date -Is)" | tee -a "$RUN_DIR/summary.log"

