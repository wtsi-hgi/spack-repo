# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafetycharts(RPackage):
	"""Charts for Monitoring Clinical Trial Safety

	Contains chart code for monitoring clinical trial safety. Charts can be used as standalone output, but are also designed for use with the 'safetyGraphics' package, which makes it easy to load data and customize the charts using an interactive web-based interface created with Shiny.
	"""
	
	homepage = "https://github.com/SafetyGraphics/safetyCharts"
	cran = "safetyCharts" 

	version("0.3.0", md5="4bfab232fe630ddabfca9bffb35c2c00")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-huxtable", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pharmartf", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tendril", type=("build", "run"))
	depends_on("r-tplyr", type=("build", "run"))
