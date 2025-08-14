#!/usr/bin/env bash

# Install packages listed in errors.txt sequentially with specific versions
# and write failures to errors.revised.txt.

set -uo pipefail

INPUT_FILE="/home/ubuntu/spack-repo/errors.txt"
REVISED_ERRORS_FILE="/home/ubuntu/spack-repo/errors.revised.txt"
INSTALL_LOG_FILE="/home/ubuntu/spack-repo/install.log"
LOGS_DIR="/home/ubuntu/spack-repo/install_logs"

SPACK_BIN=spack

if [[ ! -f "$INPUT_FILE" ]]; then
  echo "ERROR: input file not found: $INPUT_FILE" >&2
  exit 1
fi

# Create logs directory
mkdir -p "$LOGS_DIR"

# Reset outputs
: > "$REVISED_ERRORS_FILE"
{
  echo "==== $(date -u +"%Y-%m-%dT%H:%M:%SZ") Starting installs from $INPUT_FILE ===="
} > "$INSTALL_LOG_FILE"

total=0
success=0
fail=0

while IFS= read -r raw_line || [[ -n "$raw_line" ]]; do
  # Normalize/clean the line: strip comments, CR, and surrounding whitespace
  line=$(printf '%s' "$raw_line" \
    | sed -e 's/#.*$//' -e 's/\r$//' -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

  # skip empty lines
  if [[ -z "$line" ]]; then
    continue
  fi

  total=$((total + 1))

  # Split using '@' if present; otherwise fall back to last '-' delimiter
  if [[ "$line" == *"@"* ]]; then
    name="${line%%@*}"
    version="${line##*@}"
  else
    name="${line}"
    version=""
  fi

  if [[ -z "$version" ]]; then
    spec="${name} ^r@4.5:"
  else
    spec="${name}@${version} ^r@4.5:"
  fi

  echo "\n==> [$total] Installing $spec" | tee -a "$INSTALL_LOG_FILE"

  # Create individual log file for this package
  package_log_file="${LOGS_DIR}/${name}-${version}.log"
  echo "==== $(date -u +"%Y-%m-%dT%H:%M:%SZ") Installing $spec ====" > "$package_log_file"
  echo "Command: $SPACK_BIN install -y --reuse $spec" >> "$package_log_file"
  echo "" >> "$package_log_file"

  # Attempt install; capture output to both main log and individual log
  if "$SPACK_BIN" install -y --reuse "$spec" 2>&1 | tee -a "$package_log_file" "$INSTALL_LOG_FILE"; then
    echo "OK: $spec" | tee -a "$INSTALL_LOG_FILE"
    success=$((success + 1))
    # Remove individual log file for successful installs to save space
    rm -f "$package_log_file"
  else
    echo "FAIL: $spec" | tee -a "$INSTALL_LOG_FILE"
    echo "FAIL: $spec" >> "$package_log_file"
    echo "Individual log saved to: $package_log_file" | tee -a "$INSTALL_LOG_FILE"
    echo "$line" >> "$REVISED_ERRORS_FILE"
    fail=$((fail + 1))
  fi
done < "$INPUT_FILE"

echo "\n==== Completed $(date -u +"%Y-%m-%dT%H:%M:%SZ") ====" | tee -a "$INSTALL_LOG_FILE"
echo "Summary: total=$total success=$success fail=$fail" | tee -a "$INSTALL_LOG_FILE"
echo "Revised errors written to: $REVISED_ERRORS_FILE" | tee -a "$INSTALL_LOG_FILE"
echo "Individual failure logs saved to: $LOGS_DIR" | tee -a "$INSTALL_LOG_FILE"

exit 0

