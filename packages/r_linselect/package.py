# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinselect(RPackage):
	"""Selection of Linear Estimators

	Estimate the mean of a Gaussian vector, by choosing among a large collection of estimators,
  following the method developed by Y. Baraud, C. Giraud and S. Huet (2014) <doi:10.1214/13-AIHP539>.
  In particular it solves the problem of variable selection by choosing the best predictor among predictors emanating from different methods as lasso,
  elastic-net, adaptive lasso, pls, randomForest. Moreover, it can be applied for choosing the tuning parameter in a Gauss-lasso procedure.
	"""
	
	cran = "LINselect" 

	version("1.1.5", md5="d699f785c229748187c9fe98f0baaf4e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
