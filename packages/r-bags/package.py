# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBags(RPackage):
    """A Bayesian Approach for Geneset Selection

    R package providing functions to perform geneset significance analysis over simple cross-sectional data between 2 and 5 phenotypes of interest.
    """

    bioc = "BAGS"

    version("2.48.0", commit="4f8a29d54828061e99c746a8d6ddfea9da06c38b")
    version("2.42.0", commit="934252537dacd0e1997645a99d087569fc1be308")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-breastcancervdx", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
