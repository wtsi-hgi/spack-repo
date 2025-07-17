# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLevi(RPackage):
    """Landscape Expression Visualization Interface

    The tool integrates data from biological networks with transcriptomes, displaying a heatmap with surface curves to evidence the altered regions.
    """

    bioc = "levi"

    version("1.26.0", commit="7bd2746c0d2300ff1a88753eb2491a9477e4aeb5")
    version("1.20.0", commit="01d1e4d740d6d79b0d34c3675e542a40691d43f8")

    depends_on("r-dt@0.4:", type=("build", "run"))
    depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
    depends_on("r-colorspace@1.3.2:", type=("build", "run"))
    depends_on("r-dplyr@0.7.4:", type=("build", "run"))
    depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
    depends_on("r-httr@1.3.1:", type=("build", "run"))
    depends_on("r-igraph@1.2.1:", type=("build", "run"))
    depends_on("r-reshape2@1.4.3:", type=("build", "run"))
    depends_on("r-shiny@1.0.5:", type=("build", "run"))
    depends_on("r-shinydashboard@0.7:", type=("build", "run"))
    depends_on("r-shinyjs@1:", type=("build", "run"))
    depends_on("r-xml2@1.2:", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
