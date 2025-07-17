# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompass(RPackage):
    """Combinatorial Polyfunctionality Analysis of Single Cells

    COMPASS is a statistical framework that enables unbiased analysis of antigen-specific T-cell subsets. COMPASS uses a Bayesian hierarchical framework to model all observed cell-subsets and select the most likely to be antigen-specific while regularizing the small cell counts that often arise in multi-parameter space. The model provides a posterior probability of specificity for each cell subset and each sample, which can be used to profile a subject's immune response to external stimuli such as infection or vaccination.
    """

    bioc = "COMPASS"

    version("1.46.0", commit="a60809cd947e29f288f84ddf1a8e15787a8025c0")
    version("1.40.0", commit="3f7c45a28845e979f2caa56c9ff6719b3218f92a")

    depends_on("r@3.0.3:", type=("build", "run"))
    depends_on("r-rcpp@0.11:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-clue", type=("build", "run"))
    depends_on("r-pdist", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-coda", type=("build", "run"))
