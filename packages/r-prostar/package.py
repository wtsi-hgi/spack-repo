# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstar(RPackage):
    """Provides a GUI for DAPAR

    This package provides a GUI interface for the DAPAR package. The package Prostar (Proteomics statistical analysis with R) is a Bioconductor distributed R package which provides all the necessary functions to analyze quantitative data from label-free proteomics experiments. Contrarily to most other similar R packages, it is endowed with rich and user-friendly graphical interfaces, so that no programming skill is required.
    """

    homepage = "http://www.prostar-proteomics.org/"
    bioc = "Prostar"

    version("1.40.0", commit="5455e070ad3003e659b0817564f569e93883cf37")
    version("1.34.6", commit="8d40dcee8d768e7f0020e0fdf7c070621babd7ca")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r@4.4:", when="@1.40.0:", type=("build", "run"))
    depends_on("r-dapar@1.34.6:", type=("build", "run"))
    depends_on("r-dapardata@1.27.3:", type=("build", "run"))
    depends_on("r-rhandsontable", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinybs", type=("build", "run"))
    depends_on("r-shinyace", type=("build", "run"))
    depends_on("r-highcharter", type=("build", "run"))
    depends_on("r-htmlwidgets", type=("build", "run"))
    depends_on("r-webshot", type=("build", "run"))
    depends_on("r-shinythemes", type=("build", "run"))
    depends_on("r-later", type=("build", "run"))
    depends_on("r-shinycssloaders", type=("build", "run"))
    depends_on("r-future", type=("build", "run"))
    depends_on("r-promises", type=("build", "run"))
    depends_on("r-shinyjqui", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-vioplot", type=("build", "run"))
    depends_on("r-shinytree", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-colourpicker", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-shinywidgets", type=("build", "run"))
    depends_on("r-sass", type=("build", "run"))
    depends_on("r-rclipboard", type=("build", "run"))
    depends_on("r-markdown", type=("build", "run"))
