# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM3c(RPackage):
    """Monte Carlo Reference-based Consensus Clustering

    M3C is a consensus clustering algorithm that uses a Monte Carlo simulation to eliminate overestimation of K and can reject the null hypothesis K=1.
    """

    bioc = "M3C"

    version("1.30.0", commit="8d3fa5026aff7b3b90a3973aadcad3f65e86b3b8")
    version("1.24.0", commit="995cac9475ecd7ade255e4ff3fb77efa9712514f")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-dosnow", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-matrixcalc", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-corpcor", type=("build", "run"))
    depends_on("r-umap", type=("build", "run"))
