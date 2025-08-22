#!/usr/bin/env bash

set -euo pipefail

# Simple script to check if packages are installed using spack find and exit codes
# Usage: ./check_spack_installed.sh [package_list_file] [extra_spec] [max_jobs] [output_file]
# Runs spack find commands in parallel (default max 50 jobs)
# Outputs list of NOT installed packages to specified output file

run_spack_find() {
  local spec="$1"
  if command -v spack >/dev/null 2>&1; then
    # Use login shell to resolve functions/aliases/environment
    bash -lc "spack find $spec" >/dev/null 2>&1
    return $?
  fi
  echo "Spack not found in PATH" >&2
  return 1
}

check_package_parallel() {
  local package="$1"
  local extra_spec="$2"
  local spec="${package}${extra_spec}"
  
  if run_spack_find "$spec"; then
    echo "✓ $spec - INSTALLED"
    return 0
  else
    echo "✗ $spec - NOT INSTALLED"
    return 1
  fi
}

read_package_list() {
  local list_file="$1"
  awk '
    BEGIN { FS="\n" }
    {
      raw=$0
      # Trim leading/trailing whitespace including CRLF using POSIX classes
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", raw)
      if (raw == "" || raw ~ /^#/) next
      print raw
    }
  ' "$list_file"
}

wait_for_jobs() {
  local max_jobs="$1"
  while [[ $(jobs -r | wc -l) -ge $max_jobs ]]; do
    wait -n
  done
}

main() {
  local default_list="/home/ubuntu/spack-repo/errors.txt"
  local list_path="${1:-$default_list}"
  local extra_spec="${2:-}"
  local max_jobs="${3:-50}"
  local output_file="${4:-}"
  
  if [[ ! -f "$list_path" ]]; then
    echo "Package list not found: $list_path" >&2
    exit 1
  fi
  
  # Set default output file if not provided
  if [[ -z "$output_file" ]]; then
    if [[ "$list_path" == *.txt ]]; then
      output_file="${list_path%.txt}.revised.txt"
    else
      output_file="${list_path}.revised"
    fi
  fi

  echo "Checking packages from: $list_path"
  if [[ -n "$extra_spec" ]]; then
    echo "Extra spec: $extra_spec"
  fi
  echo "---"

  local total=0
  local installed=0
  local not_installed=0
  local results_file
  local not_installed_file
  results_file=$(mktemp)
  not_installed_file=$(mktemp)

  # Process packages in parallel
  while IFS= read -r package; do
    total=$((total + 1))
    
    # Wait if we've reached max jobs
    wait_for_jobs "$max_jobs"
    
    # Start background job
    (
      if check_package_parallel "$package" "$extra_spec"; then
        echo "INSTALLED" >> "$results_file"
      else
        echo "NOT_INSTALLED" >> "$results_file"
        echo "$package" >> "$not_installed_file"
      fi
    ) &
  done < <(read_package_list "$list_path")

  # Wait for all background jobs to complete
  wait

  # Count results
  if [[ -f "$results_file" ]]; then
    installed=$(grep -c "INSTALLED" "$results_file" || echo "0")
    not_installed=$(grep -c "NOT_INSTALLED" "$results_file" || echo "0")
    rm -f "$results_file"
  fi

  # Save not installed packages to output file
  if [[ -f "$not_installed_file" ]]; then
    mv "$not_installed_file" "$output_file"
    echo "Not installed packages saved to: $output_file"
  else
    # Create empty file if all packages are installed
    touch "$output_file"
    echo "All packages installed. Empty file created: $output_file"
  fi

  echo "---"
  echo "Summary:"
  echo "Total packages checked: $total"
  echo "Installed: $installed"
  echo "Not installed: $not_installed"
  echo "Output file: $output_file"
  
  # Exit with error code if any packages are not installed
  if [[ $not_installed -gt 0 ]]; then
    exit 1
  fi
}

main "$@"

