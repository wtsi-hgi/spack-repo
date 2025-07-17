# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowmatch(RPackage):
    """Matching and meta-clustering in flow cytometry

    Matching cell populations and building meta-clusters and templates from a collection of FC samples.
    """

    bioc = "flowMatch"

    version("1.44.0", commit="b0bab024afa6f369063bb4cc59b749055734a9e9")
    version("1.38.0", commit="abd0bebad093f41adf05e2b4ce3f0d698cc1b15d")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
