# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMelissa(RPackage):
    """Bayesian clustering and imputationa of single cell methylomes

    Melissa is a Baysian probabilistic model for jointly clustering and imputing single cell methylomes. This is done by taking into account local correlations via a Generalised Linear Model approach and global similarities using a mixture modelling approach.
    """

    bioc = "Melissa"

    version("1.24.0", commit="d232e8b5a2d2b538e379a305a90503d90920489a")
    version("1.18.0", commit="89af5fe2659515f2d53db26eac7ba1063a973f95")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-bprmeth", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rocr", type=("build", "run"))
    depends_on("r-matrixcalc", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-mcmcpack", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-truncnorm", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
