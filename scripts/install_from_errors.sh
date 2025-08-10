#!/usr/bin/env bash

# Install packages listed in errors.txt sequentially with specific versions
# and write failures to errors.revised.txt.

set -uo pipefail

INPUT_FILE="/home/ubuntu/spack-repo/errors.txt"
REVISED_ERRORS_FILE="/home/ubuntu/spack-repo/errors.revised.txt"
INSTALL_LOG_FILE="/home/ubuntu/spack-repo/install.log"

SPACK_BIN=spack

if [[ ! -f "$INPUT_FILE" ]]; then
  echo "ERROR: input file not found: $INPUT_FILE" >&2
  exit 1
fi

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

  # Split at the last hyphen only: name is everything before it, version is after it
  version="${line##*-}"
  name="${line%-${version}}"

  # Trim trailing hyphen from name if present (when line had exactly one hyphen)
  name="${name%%-}"

  if [[ -z "$name" || -z "$version" ]]; then
    echo "WARN: Could not parse line: '$raw_line'" | tee -a "$INSTALL_LOG_FILE" >&2
    echo "$raw_line" >> "$REVISED_ERRORS_FILE"
    fail=$((fail + 1))
    continue
  fi

  spec="${name}@${version}"
  echo "\n==> [$total] Installing $spec" | tee -a "$INSTALL_LOG_FILE"

  # Attempt install; do not abort on failure
  if "$SPACK_BIN" install -y --reuse "$spec" >> "$INSTALL_LOG_FILE" 2>&1; then
    echo "OK: $spec" | tee -a "$INSTALL_LOG_FILE"
    success=$((success + 1))
  else
    echo "FAIL: $spec" | tee -a "$INSTALL_LOG_FILE"
    echo "$line" >> "$REVISED_ERRORS_FILE"
    fail=$((fail + 1))
  fi
done < "$INPUT_FILE"

echo "\n==== Completed $(date -u +"%Y-%m-%dT%H:%M:%SZ") ====" | tee -a "$INSTALL_LOG_FILE"
echo "Summary: total=$total success=$success fail=$fail" | tee -a "$INSTALL_LOG_FILE"
echo "Revised errors written to: $REVISED_ERRORS_FILE" | tee -a "$INSTALL_LOG_FILE"

exit 0

