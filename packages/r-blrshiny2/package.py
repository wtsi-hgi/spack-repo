# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlrshiny2(RPackage):
	"""Interactive Document for Working with Binary Logistic Regression
Analysis

	An interactive document on  the topic of binary logistic regression  analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://analyticmodels.shinyapps.io/BinaryLogisticRegressionModelling/>.
	"""
	
	cran = "BLRShiny2" 

	version("0.1.0", md5="926b7d1d76cd6476468523ff8e6e06f7", url="https://cran.r-project.org/src/contrib/BLRShiny2_0.1.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
