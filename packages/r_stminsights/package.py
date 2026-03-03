# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStminsights(RPackage):
	"""A 'Shiny' Application for Inspecting Structural Topic Models

	This app enables interactive validation, interpretation and visualization of structural topic models from the 'stm' package by Roberts and others (2014) <doi:10.1111/ajps.12103>. It also includes helper functions for model diagnostics and extracting data from effect estimates.
	"""
	
	homepage = "https://github.com/cschwem2er/stminsights"
	cran = "stminsights" 

	version("0.4.2", md5="6436dbc3b71ea071d9144663b729e9b0")

	depends_on("r-stm@1.3.5:", type=("build", "run"))
	depends_on("r-tidygraph@1.2:", type=("build", "run"))
	depends_on("r-ggraph@2.1:", type=("build", "run"))
	depends_on("r-igraph@1.4:", type=("build", "run"))
	depends_on("r-ggrepel@0.9:", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-shinybs@0.6:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-tibble@3.2:", type=("build", "run"))
	depends_on("r-readr@2.1:", type=("build", "run"))
	depends_on("r-huge@1.3:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
