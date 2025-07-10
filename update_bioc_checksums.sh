#!/bin/bash

# Script to find and update Bioconductor R packages with MD5 checksums to SHA256
# Usage: ./update_bioc_checksums.sh

set -e

echo "==> Finding RPackage recipes with bioc properties and MD5 checksums..."

# Find all RPackage files with bioc = defined
bioc_files=$(grep -l 'bioc = "' packages/*/package.py)

# Counter for packages found and updated
found_count=0
updated_count=0

# Array to store packages that need updating
declare -a packages_to_update

echo "==> Checking each bioc package for MD5 checksums..."

for file in $bioc_files; do
    # Extract package name from file path (e.g., packages/r-annotationdbi/package.py -> r-annotationdbi)
    package_name=$(basename $(dirname "$file"))
    
    # Check if this file has MD5 checksums
    if grep -q 'md5=' "$file"; then
        echo "Found MD5 checksum in: $package_name"
        found_count=$((found_count + 1))
        packages_to_update+=("$package_name:$file")
    fi
done

echo "==> Found $found_count packages with MD5 checksums"

if [ $found_count -eq 0 ]; then
    echo "No packages with MD5 checksums found. Exiting."
    exit 0
fi

echo "==> Processing packages..."

for item in "${packages_to_update[@]}"; do
    package_name="${item%:*}"
    file="${item#*:}"
    
    echo "Processing: $package_name"
    
    # Find the latest version with MD5 checksum
    # Get all MD5 lines and extract versions, then find the first one (should be latest)
    latest_md5_line=$(grep 'md5=' "$file" | head -n1)
    
    # Extract version number from the latest MD5 line
    version=$(echo "$latest_md5_line" | sed -n 's/.*version("\([^"]*\)".*/\1/p')
    
    if [ -z "$version" ]; then
        echo "  Warning: Could not extract version for $package_name, skipping"
        continue
    fi
    
    echo "  Latest version with MD5: $version"
    echo "  Getting SHA256 checksum..."
    
    # Run spack checksum with 1 minute timeout and capture output
    checksum_output=$(timeout 60 spack checksum "$package_name" 2>/dev/null || true)
    
    # Check if timeout occurred by examining exit code
    if [ $? -eq 124 ]; then
        echo "  Warning: Checksum operation timed out after 1 minute for $package_name, skipping"
        continue
    fi
    
    if [ -z "$checksum_output" ]; then
        echo "  Warning: Could not get checksum for $package_name, skipping"
        continue
    fi
    
    # Extract SHA256 from output (look for the version we're interested in)
    sha256=$(echo "$checksum_output" | grep "version(\"$version\"" | sed -n 's/.*sha256="\([^"]*\)".*/\1/p')
    
    if [ -z "$sha256" ]; then
        echo "  Warning: Could not extract SHA256 for $package_name version $version, skipping"
        continue
    fi
    
    echo "  SHA256: $sha256"
    echo "  Updating file..."
    
    # Create backup
    cp "$file" "$file.backup"
    
    # Replace MD5 with SHA256 for this specific version only
    # Use a more precise sed command that targets the exact version line
    sed -i "/version(\"$version\".*md5=/s/md5=\"[^\"]*\"/sha256=\"$sha256\"/g" "$file"
    
    # Verify the change was made
    if grep -q "version(\"$version\".*sha256=\"$sha256\"" "$file"; then
        echo "  ✓ Successfully updated $package_name version $version"
        updated_count=$((updated_count + 1))
        rm "$file.backup"  # Remove backup if successful
    else
        echo "  ✗ Failed to update $package_name, restoring backup"
        mv "$file.backup" "$file"
    fi
    
    echo ""
done

echo "==> Summary:"
echo "Found: $found_count packages with MD5 checksums"
echo "Updated: $updated_count packages successfully"

if [ $updated_count -gt 0 ]; then
    echo ""
    echo "==> Would you like to commit these changes? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        echo "==> Staging changes..."
        git add packages/*/package.py
        
        echo "==> Committing changes..."
        git commit -m "Convert MD5 to SHA256 checksums for Bioconductor packages

Updated $updated_count RPackage recipes with bioc properties from MD5 to SHA256 checksums."
        
        echo "==> Pushing changes..."
        git push
        
        echo "✓ Changes committed and pushed successfully!"
    else
        echo "Changes staged but not committed. You can review and commit manually."
    fi
fi

echo "==> Done!" 