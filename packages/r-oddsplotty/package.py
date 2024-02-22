# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROddsplotty(RPackage):
	"""Odds Plot to Visualise a Logistic Regression Model

	Uses the outputs of a logistic regression model, from caret <https://CRAN.R-project.org/package=caret>, to build an odds plot.
    This allows for the rapid visualisation of odds plot ratios and works best with the outputs of CARET's GLM model class, by returning the final trained model. 
	"""
	
	homepage = "https://github.com/StatsGary/OddsPlotty"
	cran = "OddsPlotty" 

	version("1.0.2", md5="dd1b89ae48ad4868d325efcb80ac0526")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-mlbench", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-tidymodels", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
