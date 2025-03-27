# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwosamplemr(RPackage):
    """Two-Sample Mendelian Randomization Using GWAS Summary Data

    A package for performing Mendelian randomization using GWAS summary data.
    It uses the IEU OpenGWAS database to obtain data automatically and provides
    a wide range of methods to perform the analysis."""

    homepage = "https://github.com/MRCIEU/TwoSampleMR"
    url = "https://github.com/MRCIEU/TwoSampleMR/archive/refs/tags/v0.6.13.tar.gz"
    git = "https://github.com/MRCIEU/TwoSampleMR.git"

    version("0.5.6", sha256="c63eb008ab7ed08a6f30ccbf0c299beb31b2f5835e5e2aa1b59c5e4fe284a30c")

    depends_on("r@3.6.0:", type=("build", "run"))
    depends_on("r-bigsnpr", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-dplyr@1.0.0:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-gtable", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-htmlwidgets", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-ieugwasr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-markdown", type=("build", "run"))
    depends_on("r-meta", type=("build", "run"))
    depends_on("r-mrpresso", type=("build", "run"))
    depends_on("r-pbapply", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-psych", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-radialmr", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-rstudioapi", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
    depends_on("r-mendelianrandomization", type=("build", "run"))
    depends_on("r-mr-raps", type=("build", "run"))
    depends_on("r-car", type=("build", "run"))
    depends_on("r-randomforest", type=("build", "run"))
    depends_on("r-mrinstruments", type=("build", "run"))
    depends_on("r-mrmix", type=("build", "run"))
