# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFormods(RPackage):
	"""'Shiny' Modules for General Tasks

	'Shiny' apps can often make use of the same key elements, this package provides modules for common tasks (data upload, wrangling data, figure generation and saving the app state). These modules can react and interact as well as generate code to create reproducible analyses.
	"""
	
	homepage = "https://formods.ubiquity.tools/"
	cran = "formods" 

	version("0.1.4", md5="4d3457e952957fdc449ec26ea15cfc0c")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-onbrand@1.0.3:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
