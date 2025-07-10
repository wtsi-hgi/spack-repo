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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/microbiomeExplorer_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/microbiomeExplorer/microbiomeExplorer_1.12.0.tar.gz"]

	version("1.12.0", sha256="4d67a8092e65ffdba95504ae38e41b586039755c0f2c683bb51c6ee84a26de2f")

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
