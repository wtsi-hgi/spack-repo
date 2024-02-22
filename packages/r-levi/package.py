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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/levi_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/levi/levi_1.20.0.tar.gz"]

	version("1.20.0", md5="fff39f74d44cb186d14ebb591b3fa3a1")

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
