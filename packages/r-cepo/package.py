# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCepo(RPackage):
    """Cepo for the identification of differentially stable genes

    Defining the identity of a cell is fundamental to understand the heterogeneity of cells to various environmental signals and perturbations. We present Cepo, a new method to explore cell identities from single-cell RNA-sequencing data using differential stability as a new metric to define cell identity genes. Cepo computes cell-type specific gene statistics pertaining to differential stable gene expression.
    """

    bioc = "Cepo"

    version("1.14.0", commit="5896e7881840e6881e75f15a3c80326f5a4c7502")
    version("1.8.0", commit="5482f8e84fae5411991aabafe914cec8855b28ea")

    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
