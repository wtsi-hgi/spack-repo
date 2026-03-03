# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyr(RPackage):
	"""Data Insights Through Inbuilt R Shiny App

	It builds dynamic R shiny based dashboards to analyze any CSV files. It provides simple dashboard design to subset the data, perform exploratory data analysis and preliminary machine learning (supervised and unsupervised). It also provides filters based on columns of interest. 
	"""
	
	cran = "shinyr" 

	version("0.3.0", md5="fceffad0803d49c1cf5501d9439146c8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
