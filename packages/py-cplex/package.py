# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCplex(PythonPackage):
    """A Python interface to the CPLEX Callable Library, Community Edition"""

    homepage = "https://www.ibm.com/docs/en/icos/20.1.0?topic=cplex-setting-up-python-api"
    url = "https://files.pythonhosted.org/packages/ea/d7/8627519572fe0ba323e26d635010a33778ca730274eee437796802e4b990/cplex-22.1.1.1-cp311-cp311-manylinux1_x86_64.whl"

    version("22.1.1.1", sha256="c5c031afe9fef89c9a2ec76e0151befc8ace47ee1a21b9893939c29f5a1f5c2e", expand=False)
    
    depends_on("python@3.11", type=("build", "run"))
