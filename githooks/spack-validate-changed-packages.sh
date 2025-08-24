#!/usr/bin/env bash
set -euo pipefail

# Validate that changed packages under packages/<pkg-name> have an installed match in Spack
# Usage: spack-validate-changed-packages.sh [files...]

if ! command -v spack >/dev/null 2>&1; then
  echo "pre-commit: 'spack' command not found in PATH." >&2
  exit 1
fi

declare -a input_files=("$@")
if [ ${#input_files[@]} -eq 0 ]; then
  files=$(git diff --cached --name-only --diff-filter=ACMR)
else
  files=$(printf "%s\n" "${input_files[@]}")
fi

changed_pkgs=$(echo "$files" | awk -F/ '/^packages\// {print $2}' | sort -u)

if [ -z "$changed_pkgs" ]; then
  exit 0
fi

echo "pre-commit: validating changed packages with 'spack find'..."

failed=0
errors=""

for pkg in $changed_pkgs; do
  [ -z "$pkg" ] && continue
  echo "  - spack find ${pkg}"
  if ! output=$(spack find "$pkg" 2>&1); then
    failed=1
    errors="${errors}\n- spack find ${pkg} failed:\n${output}"
    continue
  fi
  if echo "$output" | grep -qE '==> 0 installed packages|No package matches'; then
    failed=1
    errors="${errors}\n- spack find ${pkg} found no installed packages:\n${output}"
  fi
done

if [ "$failed" -ne 0 ]; then
  echo "pre-commit: one or more package checks failed:" >&2
  printf "%b\n" "$errors" >&2
  exit 1
fi

exit 0


