# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRhe(PythonPackage):
    """Randomized Haseman–Elston regression for Multi-variance Components: Python wrappers for Gene-ENviroment Interaction Estimator. A python wrapper of the Gene-ENviroment Interaction Estimator"""

    homepage = "https://github.com/sriramlab/GENIE"
    url = "https://github.com/sriramlab/GENIE/archive/refs/tags/v.1.0.0.tar.gz"
    git = "https://github.com/sriramlab/GENIE.git"

    license("MIT")

    # The version 1.0.1 does not exist, but multiple phenotype function for
    # the python wrapper is missing from the 1.0.0 release
    version("1.0.1", commit="aff7617e188f02fec6f86aa51a539bf8a1a4b720")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-scikit-build-core +pyproject", type="build")
