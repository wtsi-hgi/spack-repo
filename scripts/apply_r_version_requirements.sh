#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="/home/ubuntu/spack-repo"
ERRORS_FILE="$ROOT_DIR/errors.txt"
FAILURES_JSON="$ROOT_DIR/install_logs/failure-reasons.json"

if ! command -v jq >/dev/null 2>&1; then
  echo "jq is required for this script" >&2
  exit 1
fi

if [[ ! -f "$ERRORS_FILE" ]]; then
  echo "Errors file not found: $ERRORS_FILE" >&2
  exit 1
fi

if [[ ! -f "$FAILURES_JSON" ]]; then
  echo "Failure reasons JSON not found: $FAILURES_JSON" >&2
  exit 1
fi

update_recipe_py() {
  local recipe_file="$1"
  local pkg_version="$2"
  local min_r="$3"

  python3 - "$recipe_file" "$pkg_version" "$min_r" << 'PYCODE'
import io, os, re, sys

recipe_path = sys.argv[1]
pkg_version = sys.argv[2]
min_r = sys.argv[3]

with open(recipe_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

desired = f'    depends_on("r@{min_r}:", when="@{pkg_version}:", type=("build", "run"))\n'

if any(line.strip() == desired.strip() for line in lines):
    sys.exit(0)

# If there is an existing depends_on for this version range on R, replace it
pattern_same_when = re.compile(r'^\s*depends_on\("r@[^\"]*:",\s*when="@' + re.escape(pkg_version) + r':",\s*type=\("build",\s*"run"\)\)\s*$')
for idx, line in enumerate(lines):
    if pattern_same_when.match(line):
        lines[idx] = desired
        with open(recipe_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        sys.exit(0)

# Find insertion anchor: after last depends_on or version line
anchor_indexes = []
for idx, line in enumerate(lines):
    if line.startswith('    depends_on(') or line.startswith('    version('):
        anchor_indexes.append(idx)

insert_at = anchor_indexes[-1] + 1 if anchor_indexes else None

# Fallback anchors
if insert_at is None:
    for idx, line in enumerate(lines):
        if line.startswith('    homepage') or line.startswith('    bioc'):
            insert_at = idx + 1
    if insert_at is None:
        insert_at = len(lines)

lines.insert(insert_at, desired)
with open(recipe_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
PYCODE
}

while IFS= read -r spec || [[ -n "$spec" ]]; do
  spec="${spec%%#*}"
  spec="${spec%%$'\r'}"
  [[ -z "$spec" ]] && continue

  # Expect format: <pkg>@<version>
  if [[ "$spec" != *"@"* ]]; then
    continue
  fi
  pkg="${spec%@*}"
  ver="${spec#*@}"

  # Lookup lowest_r_version for the package
  lowest_r=$(jq -r --arg pkg "$pkg" '.[] | select(.package==$pkg and has("lowest_r_version")) | .lowest_r_version' "$FAILURES_JSON" | head -n1 || true)
  if [[ -z "$lowest_r" || "$lowest_r" == "null" ]]; then
    continue
  fi

  recipe="$ROOT_DIR/packages/$pkg/package.py"
  if [[ ! -f "$recipe" ]]; then
    echo "Recipe not found, skipping: $recipe" >&2
    continue
  fi

  update_recipe_py "$recipe" "$ver" "$lowest_r"
  echo "Updated $pkg@$ver -> requires r@${lowest_r}:"
done < "$ERRORS_FILE"

echo "Done. Review git diff for changes."


