# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""
Example rationale: Shows conditional dependencies via when= spec selectors.

What this teaches:
- Use url= for tarball releases outside PyPI/CRAN.
- Multiple version() entries demonstrate pinning and reproducibility.
- Prefer sha256 over md5 for modern sources.
- Use depends_on("pkg", type=("build", "run")) to scope dependency roles.
- Use when= selectors (e.g., when="@1.0:") for conditional constraints.
"""
from spack.package import *

class PyCplex(PythonPackage):
    """A Python interface to the CPLEX Callable Library, Community Edition"""

    homepage = "https://www.ibm.com/docs/en/icos/20.1.0?topic=cplex-setting-up-python-api"
    url = "https://files.pythonhosted.org/packages/ea/d7/8627519572fe0ba323e26d635010a33778ca730274eee437796802e4b990/cplex-22.1.1.1-cp311-cp311-manylinux1_x86_64.whl"

    version("22.1.1.1", sha256="c5c031afe9fef89c9a2ec76e0151befc8ace47ee1a21b9893939c29f5a1f5c2e", expand=False)
    version("20.1.0.4", sha256="b88ddfa8da8f991c1f34c8937268e813025d51bdd500316b3ad7f40d73ebfca5", expand=False, url="https://files.pythonhosted.org/packages/c8/b9/70017e96cdf421a745f534a175f05caccedb1a1665656548f172764fac56/cplex-20.1.0.4-cp310-cp310-manylinux1_x86_64.whl")
    
    depends_on("python@3.11", type=("build", "run"), when="@22.1.1.1")
    depends_on("python@3.10", type=("build", "run"), when="@20.1.0.4")
