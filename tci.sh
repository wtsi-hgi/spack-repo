#!/bin/bash
set -euo pipefail

# declare repo_dir="${GITHUB_WORKSPACE:-~/spack-repo-1}";
declare repo_dir="${GITHUB_WORKSPACE:-$HOME/spack-repo-1}";
declare conf="--config repos:[$repo_dir]";
echo "==> conf: $conf";
cd "$repo_dir";
main="main"
pr="$(git log -1 --oneline | cut -d' ' -f1)"

PACKAGES="$1";
echo "Packages to process: $PACKAGES";

declare -a failed_installs=();

for pkg in $PACKAGES; do
    # Gather pkg info
    git checkout "$main" -q;

    # Skip dependency and version checks if package is new
    echo "spack $conf find "$pkg"";
    if ! spack $conf find "$pkg" >/dev/null 2>&1; then
        echo "Installing new package $pkg"

        git checkout "$pr" -q

        echo "spack $conf install "$pkg"";
        if ! spack $conf install "$pkg"; then
            failed_installs+=("$pkg");
        fi;

        continue
    fi

    echo "spack $conf info "$pkg"";
    v1=$(spack $conf info "$pkg" | sed -n '/^Safe versions:/,/^$/p' | sed '1d;$d');

    git checkout "$pr" -q;

    echo "spack $conf info "$pkg"";
    v2=$(spack $conf info "$pkg" | sed -n '/^Safe versions:/,/^$/p' | sed '1d;$d');

    # Build maps of pkg version -> link
    declare -A map1=();
    declare -A map2=();

    while IFS=' ' read -r key value; do 
        map1["$key"]="$value";
    done <<< "$v1";

    while IFS=' ' read -r key value; do 
        map2["$key"]="$value";
    done <<< "$v2";

    # Find new versions
    declare -a toinstall=();
    declare -a tocheck=();

    for key in "${!map2[@]}"; do
        if [[ ! -v map1[$key] ]] || [[ "${map1[$key]}" != "${map2[$key]}" ]]; then
            toinstall+=("$key");
        else
            tocheck+=("$key");
        fi;
    done;

    # Identify any versions with changed dependencies
    for version in "${tocheck[@]}"; do
        echo "spack $conf info "$pkg@$version"";
        pr_deps=$(awk '
        /^Run Dependencies:/ {f=1; next}
        f && /^\[/ {p=1}
        p {print}
        p && /\]$/ {exit}
    ' <<< "$(spack $conf info "$pkg@$version")")
        
        git checkout "$main" -q
        echo "spack $conf info "$pkg@$version"";
        main_deps=$(awk '
        /^================/ {f=1; next}
        f && /^\[/ {p=1}
        p {print}
        p && /\]$/ {exit}
    ' <<< "$(spack $conf info "$pkg@$version")")

        git checkout "$pr" -q;

        if [[ "$pr_deps" != "$main_deps" ]]; then
            echo "dependencies changed, should check install for $version"
            toinstall+=("$version")
        fi
    done

    # Uninstall and reinstall required versions
    for version in "${toinstall[@]}"; do
        spec="$pkg@$version";

        echo "spack $conf find "$spec"";
        if spack $conf find "$spec" >/dev/null 2>&1; then
            echo "Uninstalling $spec";
            spack $conf uninstall --force --yes-to-all "$spec";
        else
            echo "$spec not installed, skipping uninstall";
        fi;

        echo "Installing $spec";
        if ! spack $conf install "$spec"; then
            failed_installs+=("$spec");
        fi;
    done;
done;

if [ ${#failed_installs[@]} -eq 0 ]; then
    echo "No failures"
else
    echo "Failed installs:"
    for pkg in "${!failed_installs[@]}"; do
        echo "${failed_installs[$pkg]}"
    done
    exit 1
fi
