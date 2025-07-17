# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnassisjavalibs(RPackage):
    """OnassisJavaLibs, java libraries to run conceptmapper and semantic similarity

    A package that contains java libraries to call conceptmapper and compute semnatic similarity from R
    """

    bioc = "OnassisJavaLibs"

    version("1.30.0", commit="7c48cedb7b89b50203717da7c12feebff38247c4")
    version("1.24.0", commit="6cccb777889ba5a9533a7854f3a3f76974acb5ec")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-rjava", type=("build", "run"))
    depends_on("openjdk@1.8:", type=("build", "link", "run"))
