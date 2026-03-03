# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredictor(RPackage):
	"""Predictive Data Analysis System

	Perform a supervised data analysis on a database through a 'shiny' graphical interface. It includes methods such as K-Nearest Neighbors, Decision Trees, ADA Boosting, Extreme Gradient Boosting, Random Forest, Neural Networks, Deep Learning, Support Vector Machines and Bayesian Methods.
	"""
	
	homepage = "https://promidat.website/"
	cran = "predictoR" 

	version("3.0.3", md5="162f1c7818667e54389614964bb6999e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dt@0.27:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-shiny@1.7.4:", type=("build", "run"))
	depends_on("r-golem@0.3.5:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-loader@1.0.1:", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-xtable@1.8.4:", type=("build", "run"))
	depends_on("r-glmnet@4.1.6:", type=("build", "run"))
	depends_on("r-trainer@2.0.4:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-xgboost@1.7.3.1:", type=("build", "run"))
	depends_on("r-shinyace@0.4.2:", type=("build", "run"))
	depends_on("r-echarts4r@0.4.4:", type=("build", "run"))
	depends_on("r-htmltools@0.5.4:", type=("build", "run"))
	depends_on("r-rpart-plot@3.1.1:", type=("build", "run"))
	depends_on("r-colourpicker@1.1.1:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7.2:", type=("build", "run"))
	depends_on("r-shinycustomloader@0.9:", type=("build", "run"))
	depends_on("r-shinydashboardplus@2.0.3:", type=("build", "run"))
