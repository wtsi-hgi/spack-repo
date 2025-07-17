# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpp(RPackage):
    """Analyze thermal proteome profiling (TPP) experiments

    Analyze thermal proteome profiling (TPP) experiments with varying temperatures (TR) or compound concentrations (CCR).
    """

    bioc = "TPP"

    version("3.36.0", commit="a098c488e239d0196030330b04094b0f808ab9b4")
    version("3.30.0", commit="ad52ee3406a434b3dd3c297a1131d8a1c7bbbf09")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-biobroom", type=("build", "run"))
    depends_on("r-broom", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-futile-logger", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-mefa", type=("build", "run"))
    depends_on("r-nls2", type=("build", "run"))
    depends_on("r-openxlsx@2.4:", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-venndiagram", type=("build", "run"))
    depends_on("r-vgam", type=("build", "run"))
