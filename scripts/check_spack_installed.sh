#!/usr/bin/env bash

set -euo pipefail

# Bash version of scripts/check_spack_installed.py
# Produces identical JSON schema to the Python script.

# Do not use host /opt/spack/bin/spack. Prefer PATH via login shell, or Singularity spack.
run_spack_find_json() {
  local out_json="$1"
  if command -v spack >/dev/null 2>&1; then
    # Use login shell to resolve functions/aliases/environment
    bash -lc 'spack find --json' >"$out_json"
    return $?
  fi
  if command -v singularity >/dev/null 2>&1 && [[ -f "/home/ubuntu/spack.sif" ]]; then
    singularity exec --bind /mnt/data /home/ubuntu/spack.sif bash -lc 'spack find --json' >"$out_json"
    return $?
  fi
  echo "Spack not found in PATH and Singularity image not available" >&2
  return 1
}

require_jq() {
  if ! command -v jq >/dev/null 2>&1; then
    echo "Error: 'jq' is required. Please install jq and re-run." >&2
    exit 1
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
      # Split on last '-'
      if (index(raw, "-") == 0) {
        name=raw; version=""
      } else {
        # Extract name before last '-'
        name=raw
        sub(/-[^-]*$/, "", name)
        # Extract version after last '-'
        version=raw
        sub(/^.*-/, "", version)
      }
      printf "%s\t%s\t%s\n", raw, name, version
    }
  ' "$list_file"
}

main() {
  require_jq

  local default_list="/home/ubuntu/spack-repo/errors.txt"
  local list_path="${1:-$default_list}"
  if [[ ! -f "$list_path" ]]; then
    echo "Package list not found: $list_path" >&2
    exit 1
  fi

  local spack_source="PATH"

  # Fetch spack find JSON once
  local spack_json
  spack_json="$(mktemp)"
  if ! run_spack_find_json "$spack_json" 2>"$spack_json.err"; then
    echo "Failed to run spack find --json: $(head -n1 "$spack_json.err" 2>/dev/null)" >&2
    rm -f "$spack_json" "$spack_json.err"
    exit 1
  fi
  rm -f "$spack_json.err" || true

  # Normalize the JSON to a flat array of objects with stable fields
  local all_norm
  all_norm="$(mktemp)"
  jq -c '
    def name_of(m):
      if m.name? then m.name
      elif (m.spec? and m.spec.name?) then m.spec.name
      elif (m.nodes? and (m.nodes|length)>0 and m.nodes[0].name?) then m.nodes[0].name
      elif (m.short_spec? and (m.short_spec|contains("@"))) then (m.short_spec|split("@")[0])
      elif (m.long_spec? and (m.long_spec|contains("@"))) then (m.long_spec|split("@")[0])
      else (m.short_spec // m.long_spec // "") end;

    def ver_of(m):
      if m.version? then (m.version|tostring)
      elif (m.spec? and m.spec.version?) then (m.spec.version|tostring)
      elif (m.short_spec? and (m.short_spec|contains("@"))) then ((m.short_spec|split("@")[1]|split(" ")[0]))
      elif (m.long_spec? and (m.long_spec|contains("@"))) then ((m.long_spec|split("@")[1]|split(" ")[0]))
      else "" end;

    def norm(m): {
      name: name_of(m),
      version: ver_of(m),
      hash: (m.hash // (m.spec.hash? // null) // ((m.nodes[0]? // {})|.hash // null)),
      full_hash: (m.full_hash // (m.spec.full_hash? // null) // ((m.nodes[0]? // {})|.full_hash // null)),
      arch: (m.arch // (m.spec.arch? // null) // ((m.nodes[0]? // {})|.arch // null)),
      compiler: (m.compiler // (m.spec.compiler? // null) // ((m.nodes[0]? // {})|.compiler // null)),
      prefix: (m.prefix // m.path // (m.spec.prefix? // null) // ((m.nodes[0]? // {})|.prefix // null)),
      short_spec: (m.short_spec // ""),
      long_spec: (m.long_spec // "")
    };

    if type=="object" and .results? then .results[]?.matches[]? | norm(.)
    elif type=="array" then .[]? | norm(.)
    else empty end
  ' "$spack_json" | jq -s '.' >"$all_norm"

  # Build results array
  # We'll collect entries line-by-line and combine at the end to avoid jq --argjson pitfalls
  local results_items
  results_items="$(mktemp)"

  local total_requested=0
  while IFS=$'\t' read -r raw name version; do
    total_requested=$((total_requested + 1))

    # Installed versions for this name
    local installed_versions
    installed_versions=$(jq -c --arg name "$name" '[ .[] | select(.name==$name and (.version|length)>0) | .version ] | unique | sort' "$all_norm")

    # Details filtered
    local details
    if [[ -n "$version" ]]; then
      details=$(jq -c --arg name "$name" --arg version "$version" '[ .[] | select(.name==$name and .version==$version) ]' "$all_norm")
    else
      details=$(jq -c --arg name "$name" '[ .[] | select(.name==$name) ]' "$all_norm")
    fi

    local matches_count installed
    matches_count=$(echo "$details" | jq 'length')
    if [[ "$matches_count" -gt 0 ]]; then
      installed=true
    else
      installed=false
    fi

    local spec_requested
    if [[ -n "$version" ]]; then
      spec_requested="${name}@${version}"
    else
      spec_requested="$name"
    fi

    # Construct entry JSON
    local entry
    entry=$(jq -c -n \
      --arg raw "$raw" \
      --arg name "$name" \
      --arg version_requested "$version" \
      --arg spec_requested "$spec_requested" \
      --argjson details "$details" \
      --argjson installed_versions "$installed_versions" \
      --argjson matches_count "$matches_count" \
      --arg installed "$installed" \
      '{
        raw: $raw,
        name: $name,
        version_requested: $version_requested,
        spec_requested: $spec_requested,
        installed: ($installed=="true"),
        matches_count: $matches_count,
        installed_versions_for_name: $installed_versions,
        details: $details
      }')
    echo "$entry" >> "$results_items"
  done < <(read_package_list "$list_path")

  # Emit final report JSON
  local results
  results=$(jq -s -c '.' "$results_items")
  jq -n \
    --arg source_file "$list_path" \
    --arg spack "$spack_source" \
    --argjson total_requested "$total_requested" \
    --arg generated_by "check_spack_installed.sh" \
    --argjson results "$results" \
    '{
      source_file: $source_file,
      spack: $spack,
      total_requested: $total_requested,
      generated_by: $generated_by,
      results: $results
    }'

  rm -f "$spack_json" "$all_norm" "$results_items"
}

main "$@"

