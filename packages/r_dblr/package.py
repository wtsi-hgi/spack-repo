# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDblr(RPackage):
	"""Discrete Boosting Logistic Regression

	Trains logistic regression model by discretizing continuous variables via gradient boosting approach. The proposed method tries to achieve a tradeoff between interpretation and prediction accuracy for logistic regression by discretizing the continuous variables. The variable binning is accomplished in a supervised fashion. The model trained by this package is still a single 
  logistic regression model, but not a sequence of logistic regression models. The fitted model
  object returned from the model training consists of two tables. One table is used to give the
  boundaries of bins for each continuous variable as well as the corresponding coefficients,
  and the other one is used for discrete variables. This package can also be used for binning
  continuous variables for other statistical analysis. 
	"""
	
	cran = "dblr" 

	version("0.1.0", md5="b7aa629981e70149379de8c045a6a755")

	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-xgboost@0.6.4:", type=("build", "run"))
	depends_on("r-catencoders@0.1.1:", type=("build", "run"))
	depends_on("r-metrics@0.1.1:", type=("build", "run"))
