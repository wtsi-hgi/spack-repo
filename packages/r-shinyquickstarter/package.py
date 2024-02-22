# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyquickstarter(RPackage):
	"""'RStudio' Addin for Building Shiny Apps per Drag & Drop

	This 'RStudio' addin makes the creation of 'Shiny' and 'ShinyDashboard' apps more efficient.  Besides the necessary folder structure, entire apps can be created using a drag and drop interface and customized with respect to a specific use case. The addin allows the export of the required user interface and server code at any time. By allowing the creation of modules, the addin can be used throughout the entire app development process.
	"""
	
	cran = "ShinyQuickStarter" 

	version("2.0.1", md5="bdd100d4d1aefda86d19741e18d25678")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7:", type=("build", "run"))
	depends_on("r-shinywidgets@0.5.7:", type=("build", "run"))
	depends_on("r-miniui@0.1.1.1:", type=("build", "run"))
	depends_on("r-shinyjs@2:", type=("build", "run"))
	depends_on("r-shinyfiles@0.9:", type=("build", "run"))
	depends_on("r-shinyalert@2:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-colourpicker@1.1:", type=("build", "run"))
	depends_on("r-plotly@4.9:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-stringi@1.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-styler@1.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
