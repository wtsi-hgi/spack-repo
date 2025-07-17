# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyepico(RPackage):
    """ShinyÉPICo

    ShinyÉPICo is a graphical pipeline to analyze Illumina DNA methylation arrays (450k or EPIC). It allows to calculate differentially methylated positions and differentially methylated regions in a user-friendly interface. Moreover, it includes several options to export the results and obtain files to perform downstream analysis.
    """

    homepage = "https://github.com/omorante/shiny_epico"
    bioc = "shinyepico"

    version("1.16.0", commit="81e52f451c3befd336f219ed871b09271fe52ed6")
    version("1.10.0", commit="1ddbe37a580db7c309236e15f9594ed0eb01df41")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-dt@0.15:", type=("build", "run"))
    depends_on("r-data-table@1.13:", type=("build", "run"))
    depends_on("r-doparallel@1:", type=("build", "run"))
    depends_on("r-dplyr@1.0.9:", type=("build", "run"))
    depends_on("r-foreach@1.5:", type=("build", "run"))
    depends_on("r-genomicranges@1.38:", type=("build", "run"))
    depends_on("r-ggplot2@3.3:", type=("build", "run"))
    depends_on("r-gplots@3:", type=("build", "run"))
    depends_on("r-heatmaply@1.1:", type=("build", "run"))
    depends_on("r-limma@3.42:", type=("build", "run"))
    depends_on("r-minfi@1.32:", type=("build", "run"))
    depends_on("r-plotly@4.9.2:", type=("build", "run"))
    depends_on("r-reshape2@1.4:", type=("build", "run"))
    depends_on("r-rlang@1.0.2:", type=("build", "run"))
    depends_on("r-rmarkdown@2.3:", type=("build", "run"))
    depends_on("r-rtracklayer@1.46:", type=("build", "run"))
    depends_on("r-shiny@1.5:", type=("build", "run"))
    depends_on("r-shinywidgets@0.5:", type=("build", "run"))
    depends_on("r-shinycssloaders@0.3:", type=("build", "run"))
    depends_on("r-shinyjs@1.1:", type=("build", "run"))
    depends_on("r-shinythemes@1.1:", type=("build", "run"))
    depends_on("r-statmod@1.4:", type=("build", "run"))
    depends_on("r-tidyr@1.2:", type=("build", "run"))
    depends_on("r-zip@2.1:", type=("build", "run"))
