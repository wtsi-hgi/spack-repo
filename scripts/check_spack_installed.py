#!/usr/bin/env python3

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def find_spack_executable() -> str:
    candidates = [
        "/opt/spack/bin/spack",
        shutil.which("spack"),
    ]
    for candidate in candidates:
        if candidate and os.path.exists(candidate):
            return candidate
    raise RuntimeError(
        "Spack executable not found. Expected at /opt/spack/bin/spack or in PATH."
    )


def read_package_list(file_path: Path) -> list[tuple[str, str, str]]:
    """
    Read lines like "<name>-<version>" and return triples of (raw, name, version).
    Splits on the last '-' only.
    Ignores empty lines and lines starting with '#'.
    """
    packages: list[tuple[str, str, str]] = []
    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            raw = line.strip()
            if not raw or raw.startswith("#"):
                continue
            if "-" not in raw:
                # No version provided; treat as name only
                name, version = raw, ""
            else:
                # split on last '-'
                idx = raw.rfind("-")
                name, version = raw[:idx], raw[idx + 1 :]
            packages.append((raw, name, version))
    return packages


def run_spack_find_all(spack_exe: str) -> dict:
    """Return parsed JSON for all installed packages via `spack find --json`."""
    proc = subprocess.run(
        [spack_exe, "find", "--json"],
        check=False,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"spack find failed: {proc.stderr.strip()}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse JSON from `spack find --json`: {e}")


def extract_matches_map(all_find_json) -> dict[str, list[dict]]:
    """
    Build a mapping: name -> list of match dicts.
    Tolerates structure differences across Spack versions.
    """
    name_to_matches: dict[str, list[dict]] = {}

    # Case 1: Dict with "results" → entries with "matches"
    if isinstance(all_find_json, dict):
        results = all_find_json.get("results", [])
        for res in results:
            matches = res.get("matches", [])
            for m in matches:
                name = (
                    m.get("name")
                    or (m.get("spec") or {}).get("name")
                    or (m.get("nodes", [{}])[0] or {}).get("name")
                )
                if not name:
                    short_spec = m.get("short_spec") or m.get("long_spec") or ""
                    name = short_spec.split("@")[0] if "@" in short_spec else short_spec
                if not name:
                    continue
                name_to_matches.setdefault(name, []).append(m)
        return name_to_matches

    # Case 2: Top-level is a list of matches/specs
    if isinstance(all_find_json, list):
        for m in all_find_json:
            name = (
                (m.get("name") if isinstance(m, dict) else None)
                or ((m.get("spec") or {}).get("name") if isinstance(m, dict) else None)
                or ((m.get("nodes", [{}])[0] or {}).get("name") if isinstance(m, dict) else None)
            )
            if not name and isinstance(m, dict):
                short_spec = m.get("short_spec") or m.get("long_spec") or ""
                name = short_spec.split("@")[0] if "@" in short_spec else short_spec
            if not name:
                continue
            name_to_matches.setdefault(name, []).append(m)
        return name_to_matches

    # Fallback: unknown shape
    return name_to_matches


def get_version_from_match(m: dict) -> str:
    v = m.get("version")
    if v:
        return str(v)
    spec = m.get("spec") or {}
    v = spec.get("version")
    if v:
        return str(v)
    short = m.get("short_spec") or m.get("long_spec") or ""
    if "@" in short:
        after = short.split("@", 1)[1]
        return after.split()[0]
    return ""


def get_match_details(m: dict) -> dict:
    spec = m.get("spec") or {}
    nodes = m.get("nodes") or []
    node0 = nodes[0] if nodes else {}
    return {
        "name": m.get("name") or spec.get("name") or node0.get("name"),
        "version": get_version_from_match(m),
        "hash": m.get("hash") or spec.get("hash") or node0.get("hash"),
        "full_hash": m.get("full_hash") or spec.get("full_hash") or node0.get("full_hash"),
        "arch": m.get("arch") or spec.get("arch") or node0.get("arch"),
        "compiler": m.get("compiler") or spec.get("compiler") or node0.get("compiler"),
        "prefix": m.get("prefix") or m.get("path") or spec.get("prefix") or node0.get("prefix"),
        "short_spec": m.get("short_spec") or "",
        "long_spec": m.get("long_spec") or "",
    }


def main() -> int:
    # Determine inputs
    default_list = Path("/home/ubuntu/spack-repo/errors.txt")
    list_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_list

    spack_exe = find_spack_executable()
    package_entries = read_package_list(list_path)

    # Load all installs once for speed
    all_find_json = run_spack_find_all(spack_exe)
    name_to_matches = extract_matches_map(all_find_json)

    report = {
        "source_file": str(list_path),
        "spack": spack_exe,
        "total_requested": len(package_entries),
        "generated_by": "check_spack_installed.py",
        "results": [],
    }

    for raw, name, version in package_entries:
        matches_for_name = name_to_matches.get(name, [])
        # filter by exact version if provided
        filtered = (
            [m for m in matches_for_name if version and get_version_from_match(m) == version]
            if version
            else matches_for_name
        )
        installed_versions = sorted({get_version_from_match(m) for m in matches_for_name if get_version_from_match(m)})

        report["results"].append(
            {
                "raw": raw,
                "name": name,
                "version_requested": version,
                "spec_requested": f"{name}@{version}" if version else name,
                "installed": len(filtered) > 0,
                "matches_count": len(filtered),
                "installed_versions_for_name": installed_versions,
                "details": [get_match_details(m) for m in filtered],
            }
        )

    json.dump(report, sys.stdout, indent=2, sort_keys=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

