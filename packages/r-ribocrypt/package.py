# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRibocrypt(RPackage):
    """Interactive visualization in genomics

    R Package for interactive visualization and browsing NGS data. It contains a browser for both transcript and genomic coordinate view. In addition a QC and general metaplots are included, among others differential translation plots and gene expression plots. The package is still under development.
    """

    homepage = "https://github.com/m-swirski/RiboCrypt"
    bioc = "RiboCrypt"

    version("1.14.0", commit="1ecf9fe0ab3129f37ba5249c7576f057a1381dc9")
    version("1.8.0", commit="f2d42178d09ee884180d4482e10756bf98b95bef")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-orfik@1.13.12:", type=("build", "run"))
    depends_on("r-bslib", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-htmlwidgets", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-markdown", type=("build", "run"))
    depends_on("r-nglviewer", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-rclipboard", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-writexl", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinycssloaders", type=("build", "run"))
    depends_on("r-shinyhelper", type=("build", "run"))
    depends_on("r-shinyjqui", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
