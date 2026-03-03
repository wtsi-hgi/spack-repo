# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErsa(RPackage):
	"""Exploratory Regression 'Shiny' App

	Constructs a 'shiny' app function with interactive displays for summary and analysis of variance regression tables, and parallel coordinate plots of data and residuals.
	"""
	
	cran = "ERSA" 

	version("0.1.4", md5="5cd3e6ed8871e4bf7669acaee7c9bc95")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
