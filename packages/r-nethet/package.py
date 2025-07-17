# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNethet(RPackage):
    """A bioconductor package for high-dimensional exploration of biological network heterogeneity

    Package nethet is an implementation of statistical solid methodology enabling the analysis of network heterogeneity from high-dimensional data. It combines several implementations of recent statistical innovations useful for estimation and comparison of networks in a heterogeneous, high-dimensional setting. In particular, we provide code for formal two-sample testing in Gaussian graphical models (differential network and GGM-GSA; Stadler and Mukherjee, 2013, 2014) and make a novel network-based clustering algorithm available (mixed graphical lasso, Stadler and Mukherjee, 2013).
    """

    bioc = "nethet"

    version("1.40.0", commit="73905001f75fde0d48359f791629717acd1c4893")
    version("1.34.0", commit="e771f90ca4b4bd705b1a557fda9cc38ec58a2b96")

    depends_on("r-glasso", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-genenet", type=("build", "run"))
    depends_on("r-huge", type=("build", "run"))
    depends_on("r-compquadform", type=("build", "run"))
    depends_on("r-ggm", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-gsa", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-multtest", type=("build", "run"))
    depends_on("r-icsnp", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-network", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
