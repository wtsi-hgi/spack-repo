#!/bin/bash

# Script to add RELEASE_3_21 version lines to Bioconductor R package recipes missing them
# Usage: ./add_bioc_release_3_21_versions.sh

set -e

SCRATCH_DIR="/tmp/scratch"

# Find all RPackage files with bioc = defined
bioc_files=$(grep -l 'bioc = ' packages/*/package.py)

added_count=0

echo "==> Scanning for Bioconductor R packages missing RELEASE_3_21..."

for file in $bioc_files; do
    # Skip if any version line contains RELEASE_3_21
    if grep -q 'version(.*RELEASE_3_21' "$file"; then
        continue
    fi

    # Extract package name from bioc = "..." line
    bioc_pkg=$(grep 'bioc = ' "$file" | sed -n 's/.*bioc = "\([^"]*\)".*/\1/p')
    if [ -z "$bioc_pkg" ]; then
        echo "  Could not extract bioc package name from $file, skipping"
        continue
    fi
    echo "Processing $bioc_pkg ($file)"

    # Remove previous scratch dir
    rm -rf "$SCRATCH_DIR"

    # Clone the Bioconductor repo
    git clone --quiet https://git.bioconductor.org/packages/$bioc_pkg "$SCRATCH_DIR"
    if [ ! -d "$SCRATCH_DIR" ]; then
        echo "  Failed to clone $bioc_pkg, skipping"
        continue
    fi

    cd "$SCRATCH_DIR"
    # Check if tag exists
    if ! git rev-parse --verify --quiet RELEASE_3_21 >/dev/null; then
        echo "  Tag RELEASE_3_21 not found for $bioc_pkg, skipping"
        cd - >/dev/null
        continue
    fi
    git checkout --quiet RELEASE_3_21

    # Extract Version from DESCRIPTION
    if [ ! -f DESCRIPTION ]; then
        echo "  No DESCRIPTION file in $bioc_pkg, skipping"
        cd - >/dev/null
        continue
    fi
    version=$(grep '^Version:' DESCRIPTION | awk '{print $2}')
    if [ -z "$version" ]; then
        echo "  Could not extract Version from DESCRIPTION, skipping"
        cd - >/dev/null
        continue
    fi
    cd - >/dev/null

    # Add version line to the recipe (before the first version() line)
    insert_line="    version(\"$version\", tag=\"RELEASE_3_21\")"
    # Find first version() line number
    first_version_line=$(grep -n 'version(' "$file" | head -n1 | cut -d: -f1)
    if [ -z "$first_version_line" ]; then
        echo "  No version() lines found in $file, skipping"
        continue
    fi
    # Insert before first version() line
    awk -v n=$first_version_line -v s="$insert_line" 'NR==n{print s; print; next} 1' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
    echo "  ✓ Added: $insert_line"
    added_count=$((added_count + 1))
done

echo "==> Added RELEASE_3_21 version lines to $added_count recipes." 