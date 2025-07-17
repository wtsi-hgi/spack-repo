# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQplexanalyzer(RPackage):
    """Tools for quantitative proteomics data analysis

    Tools for TMT based quantitative proteomics data analysis.
    """

    bioc = "qPLEXanalyzer"

    version("1.26.0", commit="a88b504099c634739a598cc6feb3e1e5ab10f916")
    version("1.20.0", commit="18ccb64100b41d44d75c7a73ab4545136bef8f91")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-msnbase", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-dplyr@1:", type=("build", "run"))
    depends_on("r-ggdendro", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-preprocesscore", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
