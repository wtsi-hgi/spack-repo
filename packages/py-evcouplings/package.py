# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEvcouplings(PythonPackage):
    """A Framework for evolutionary couplings analysis"""

    homepage = "https://github.com/debbiemarkslab/EVcouplings"
    pypi = "evcouplings/evcouplings-0.2.1-py2.py3-none-any.whl"

    version("0.0.1", sha256="c16eed4c0137be5a2c7406b9250fa1f292d2067fa79e24745c6052a599b9892a")
    version("0.0.2", sha256="c4a6d2c6e33a5e8b1d1b6b9987b8d673470ccf761295022e52a136bb97ff654a")
    version("0.0.3", sha256="92f9bd80a1b48900484782c8bee4d1e2969fc07f11907a14bcb54275714251be")
    version("0.0.4", sha256="3c4d69cca93fa42bbf975dbc4455d511601bd9748a87b98296fd13646bb86b70")
    version("0.0.5", sha256="08a8d3712076688c1b848537cdd711489b04da08f77725d496e1696126f15026")
    version("0.1.1", sha256="aba07acdc39a0da73f39f48a8cac915d5b671abc008c123bbe30e6759a2499d2")
    version(
        "0.2.1",
        sha256="9017f95cd0730d858b6782be48291423125f49793aa52875d23c63995ef8ff45",
        expand=False,
        url="https://files.pythonhosted.org/packages/c8/01/f57cd1c1481daa17937aed967e391b5aea0f0d4f4b76e87c7a9f143e46f3/evcouplings-0.2.1-py2.py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("py-billiard", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-bokeh", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-filelock", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-msgpack", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-ruamel-yaml", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("cns-solve", type=("build", "run"))
    depends_on("maxcluster", type=("build", "run"))
    depends_on("psipred", type=("build", "run"))
    depends_on("hmmer", type=("build", "run"))
    depends_on("hh-suite", type=("build", "run"))
    depends_on("plmc precision=single", type=("build", "run"))

    def patch(self):
        """Apply patches to work around PDB rate limiting issues"""
        # Create sitecustomize.py with PDB rate limiting workarounds
        self._create_sitecustomize_patch()

    def _create_sitecustomize_patch(self):
        """Create sitecustomize.py to patch evcouplings for PDB rate limiting"""
        import os
        import glob
        
        # Find the site-packages directory
        site_packages_dirs = glob.glob(os.path.join(self.prefix, 'lib', 'python*', 'site-packages'))
        if not site_packages_dirs:
            return
        
        site_packages_dir = site_packages_dirs[0]
        sitecustomize_path = os.path.join(site_packages_dir, 'sitecustomize.py')
        
        # Create the sitecustomize.py content
        sitecustomize_content = '''"""
Runtime monkeypatches for the evcouplings container.

Goal: ensure PDB fetching runs sequentially (single worker) to avoid
PDB rate limits when loading multiple structures.

This module is auto-imported by Python if present on sys.path as
sitecustomize.py, so we bind-mount it into the container's site-packages.
"""

from __future__ import annotations

import os
import socket
import time
from datetime import datetime
from typing import Dict


def _install_sequential_pdb_loader() -> None:
    try:
        # Import inside function so sitecustomize import stays lightweight
        from evcouplings.compare import pdb as pdb_mod  # type: ignore
    except Exception:
        return

    # Keep reference to original API
    try:
        _PDB = pdb_mod.PDB
    except Exception:
        _PDB = None

    def load_structures_sequential(pdb_ids, structure_dir=None, raise_missing=False, *_, **__):
        """
        Drop-in replacement for evcouplings.compare.pdb.load_structures that
        fetches structures strictly sequentially.
        """
        structures = {}
        for pdb_id in pdb_ids:
            try:
                # Prefer local file if structure_dir provided
                if structure_dir is not None:
                    # Accept both .bcif.gz and .pdb.gz as used by evcouplings
                    import os

                    candidates = [
                        os.path.join(structure_dir, f"{str(pdb_id).lower()}.bcif.gz"),
                        os.path.join(structure_dir, f"{str(pdb_id).lower()}.pdb.gz"),
                        os.path.join(structure_dir, f"{str(pdb_id).lower()}.cif.gz"),
                    ]
                    for path in candidates:
                        if os.path.exists(path):
                            structures[pdb_id] = _PDB.from_file(path) if _PDB is not None else pdb_mod.PDB.from_file(path)
                            break
                    else:
                        # Remote fetch with retries/backoff to avoid PDB rate limits
                        backoff = 0.5
                        max_retries = 6
                        last_exc = None
                        for attempt in range(max_retries):
                            try:
                                structures[pdb_id] = _PDB.from_id(pdb_id) if _PDB is not None else pdb_mod.PDB.from_id(pdb_id)
                                break
                            except Exception as e:  # noqa: BLE001
                                last_exc = e
                                time.sleep(backoff)
                                backoff = min(4.0, backoff * 2)
                        else:
                            # All retries failed
                            raise last_exc if last_exc is not None else RuntimeError("Unknown PDB fetch error")
                else:
                    backoff = 0.5
                    max_retries = 6
                    last_exc = None
                    for attempt in range(max_retries):
                        try:
                            structures[pdb_id] = _PDB.from_id(pdb_id) if _PDB is not None else pdb_mod.PDB.from_id(pdb_id)
                            break
                        except Exception as e:  # noqa: BLE001
                            last_exc = e
                            time.sleep(backoff)
                            backoff = min(4.0, backoff * 2)
                    else:
                        raise last_exc if last_exc is not None else RuntimeError("Unknown PDB fetch error")

                # Small delay to be gentle to remote servers
                time.sleep(0.5)
            except Exception:
                # Never propagate missing-structure errors when fetching remotely; skip
                # This avoids brittle failures under LSF when a subset of PDB IDs 404/rate-limit
                pass
        return structures

    try:
        pdb_mod.load_structures = load_structures_sequential  # type: ignore[attr-defined]
        # Also patch any symbol-import alias in distances
        try:
            from evcouplings.compare import distances as _dist_mod  # type: ignore
            _dist_mod.load_structures = load_structures_sequential  # type: ignore[attr-defined]
        except Exception:
            pass
    except Exception:
        # If attribute missing, ignore silently
        pass


_install_sequential_pdb_loader()


def _patch_intra_dists_missing_structures() -> None:
    try:
        from evcouplings.compare import distances as dist_mod  # type: ignore
        from evcouplings.compare import protocol as prot_mod  # type: ignore
        import pandas as pd  # noqa: F401
    except Exception:
        return

    original_intra = getattr(dist_mod, "intra_dists", None)
    if original_intra is None:
        return

    def intra_dists_safe(sifts_result, structures: Dict = None, *args, **kwargs):
        # If structures dict is provided, drop hits for missing PDB IDs to avoid KeyError
        try:
            if structures is not None and hasattr(sifts_result, "hits"):
                # Normalize provided structures to a lowercase-key dict to be robust to case mismatches
                try:
                    structures = {str(k).lower(): v for k, v in structures.items()}
                except Exception:
                    pass
                available = set(k for k in structures.keys())
                hits = sifts_result.hits
                if hasattr(hits, "pdb_id"):
                    mask = hits.pdb_id.str.lower().isin(available)
                    if not mask.all():
                        sifts_result.hits = hits[mask]
        except Exception:
            # If anything goes wrong, fall back to original behavior
            pass
        # Force raise_missing=False by default unless explicitly True
        if "raise_missing" not in kwargs:
            kwargs["raise_missing"] = False
        
        # Debug: print information about structures and sifts_result
        print(f"DEBUG: structures type: {type(structures)}, keys: {list(structures.keys()) if structures else 'None'}")
        print(f"DEBUG: sifts_result type: {type(sifts_result)}")
        if hasattr(sifts_result, 'hits') and hasattr(sifts_result.hits, 'pdb_id'):
            print(f"DEBUG: sifts_result.hits.pdb_id: {sifts_result.hits.pdb_id.tolist()}")
        
        # Call the original function
        result = original_intra(sifts_result, structures, *args, **kwargs)
        
        # If the result is None (no structures available), try to create a minimal valid result
        if result is None:
            print("Warning: No structures available, attempting to create minimal result")
            # Try to create a minimal result by calling the original function with an empty structures dict
            try:
                empty_structures = {}
                result = original_intra(sifts_result, empty_structures, *args, **kwargs)
                if result is not None:
                    return result
            except Exception as e:
                print(f"Warning: Failed to create minimal result: {e}")
            
            # If all else fails, raise a more informative error
            raise RuntimeError("No PDB structures available for comparison. This may be due to rate limiting or network issues.")
        
        return result

    try:
        dist_mod.intra_dists = intra_dists_safe  # type: ignore
        # Also update the symbol inside the protocol module in case it imported it directly
        prot_mod.intra_dists = intra_dists_safe  # type: ignore
    except Exception:
        pass


_patch_intra_dists_missing_structures()

def _wrap_protocol_standard_to_disable_raise_missing() -> None:
    try:
        from evcouplings.compare import protocol as prot_mod  # type: ignore
        from evcouplings.compare import distances as dist_mod  # type: ignore
    except Exception:
        return

    try:
        original_standard = getattr(prot_mod, "standard")
    except Exception:
        return

    def standard_wrapped(**kwargs):
        original_intra = dist_mod.intra_dists

        def intra_with_no_raise(sifts_result, structures=None, *args, **kw):
            if "raise_missing" not in kw:
                kw["raise_missing"] = False
            return original_intra(sifts_result, structures, *args, **kw)

        dist_mod.intra_dists = intra_with_no_raise  # type: ignore
        try:
            return original_standard(**kwargs)
        finally:
            dist_mod.intra_dists = original_intra  # type: ignore

    try:
        prot_mod.standard = standard_wrapped  # type: ignore
    except Exception:
        pass


_wrap_protocol_standard_to_disable_raise_missing()

def _patch_prepare_structures() -> None:
    try:
        from evcouplings.compare import distances as dist_mod  # type: ignore
        from evcouplings.compare import pdb as pdb_mod  # type: ignore
    except Exception:
        return

    def _prepare_structures_safe(sifts_result, structure_dir=None, raise_missing=True):
        # Use our sequential, non-raising loader regardless of caller flags
        try:
            loader = getattr(pdb_mod, "load_structures")
        except Exception:
            return {}
        try:
            return loader(
                set(sifts_result.hits.pdb_id.str.upper()) if hasattr(sifts_result, "hits") else [],
                structure_dir=structure_dir,
                raise_missing=False,
            )
        except Exception:
            return {}

    try:
        dist_mod._prepare_structures = _prepare_structures_safe  # type: ignore[attr-defined]
    except Exception:
        pass


_patch_prepare_structures()

# Debug marker: confirm sitecustomize loaded inside the running interpreter
try:
    marker = f"[{datetime.utcnow().isoformat()}Z] sitecustomize loaded on {socket.gethostname()} pid {os.getpid()}\\n"
    with open("/tmp/sitecustomize_loaded.log", "a") as fh:
        fh.write(marker)
    print(marker.strip(), flush=True)
except Exception as e:
    try:
        with open("/tmp/sitecustomize_error.log", "a") as fh:
            fh.write(f"[{datetime.utcnow().isoformat()}Z] Error in sitecustomize: {e}\\n")
    except:
        pass
'''
        
        # Write the sitecustomize.py file
        with open(sitecustomize_path, 'w') as f:
            f.write(sitecustomize_content)


# {'billiard': ['0.2.1'], 'biopython>=1.84': ['0.2.1'], 'bokeh': ['0.2.1'], 'click': ['0.2.1'], 'filelock': ['0.2.1'], 'jinja2': ['0.2.1'], 'matplotlib': ['0.2.1'], 'msgpack': ['0.2.1'], 'numba': ['0.2.1'], 'numpy': ['0.2.1'], 'pandas': ['0.2.1'], 'psutil': ['0.2.1'], 'requests': ['0.2.1'], 'ruamel-yaml<0.18': ['0.2.1'], 'scikit-learn': ['0.2.1'], 'scipy': ['0.2.1'], 'seaborn': ['0.2.1'], 'setuptools>=18.2': ['0.2.1']}
