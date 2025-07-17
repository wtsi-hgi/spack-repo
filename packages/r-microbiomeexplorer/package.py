# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiomeexplorer(RPackage):
    """Microbiome Exploration App

    The MicrobiomeExplorer R package is designed to facilitate the analysis and visualization of marker-gene survey feature data. It allows a user to perform and visualize typical microbiome analytical workflows either through the command line or an interactive Shiny application included with the package. In addition to applying common analytical workflows the application enables automated analysis report generation.
    """

    bioc = "microbiomeExplorer"

    version("1.18.0", commit="d14da9619fd44e7e0f794f6af422254895535a9e")
    version("1.12.0", commit="83cb13161b057827c8f44cdb999c0aede136d9a6")

    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-metagenomeseq", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-shinyjs@2:", type=("build", "run"))
    depends_on("r-shinydashboard", type=("build", "run"))
    depends_on("r-shinycssloaders", type=("build", "run"))
    depends_on("r-shinywidgets", type=("build", "run"))
    depends_on("r-rmarkdown@1.9:", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-dt@0.12:", type=("build", "run"))
    depends_on("r-biomformat", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-heatmaply", type=("build", "run"))
    depends_on("r-car", type=("build", "run"))
    depends_on("r-broom", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-lubridate", type=("build", "run"))
    depends_on("r-plotly@4.9.1:", type=("build", "run"))
