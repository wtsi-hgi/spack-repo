# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCreditmodel(RPackage):
	"""Toolkit for Credit Modeling, Analysis and Visualization

	
  Provides a highly efficient R tool suite for Credit Modeling, Analysis and Visualization.Contains infrastructure functionalities such as data exploration and preparation, missing values treatment, outliers treatment, variable derivation, variable selection, dimensionality reduction, grid search for hyper parameters, data mining and visualization, model evaluation, strategy analysis etc. This package is designed to make the development of binary classification models (machine learning based models as well as credit scorecard) simpler and faster. The references including: 1 Refaat, M. (2011, ISBN: 9781447511199). Credit Risk Scorecard: Development and Implementation Using SAS; 2 Bezdek, James C.FCM: The fuzzy c-means clustering algorithm. Computers & Geosciences (0098-3004),<DOI:10.1016/0098-3004(84)90020-7>.
	"""
	
	cran = "creditmodel" 

	version("1.3.1", md5="eca08d92d7f149c8574af81b29ec87a1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
