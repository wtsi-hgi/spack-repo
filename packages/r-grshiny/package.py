# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrshiny(RPackage):
	"""Graded Response Model

	Simulation and analysis of graded response data with different types of estimators. Also, an interactive shiny application is provided with graphics for characteristic and information curves. Samejima (2018) <doi:10.1007/978-1-4757-2691-6_5>.
	"""
	
	homepage = "https://github.com/sooyongl/GRShiny"
	cran = "GRShiny" 

	version("1.0.0", md5="2ea056c139346513ba2c9feb6d42701a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-sirt", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-sass", type=("build", "run"))
