# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenerecommender(RPackage):
    """A gene recommender algorithm to identify genes coexpressed with a query set of genes

    This package contains a targeted clustering algorithm for the analysis of microarray data. The algorithm can aid in the discovery of new genes with similar functions to a given list of genes already known to have closely related functions.
    """

    bioc = "geneRecommender"

    version("1.80.0", commit="140e8f2dfc2db3138347bd3fd1895354cdc670cf")
    version("1.74.0", commit="33c46000ff67e26463b5eaa811b03b653e4ac707")

    depends_on("r@1.8:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
