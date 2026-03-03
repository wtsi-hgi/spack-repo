# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlrshiny(RPackage):
	"""Interactive Document for Working with Binary Logistic Regression
Analysis

	An interactive document on  the topic of binary logistic regression  analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://analyticmodels.shinyapps.io/BinaryLogisticRegressionModelling/>.
	"""
	
	cran = "BLRShiny" 

	version("0.1.0", md5="26ea833e08b7bd9675698268ea7c3df7")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
