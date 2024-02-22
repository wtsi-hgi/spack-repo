# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiview(RPackage):
	"""Cooperative Learning for Multi-View Analysis

	Cooperative learning combines the usual squared error loss of predictions with an agreement penalty to encourage the predictions from different data views to agree. By varying the weight of the agreement penalty, we get a continuum of solutions that include the well-known early and late fusion approaches. Cooperative learning chooses the degree of agreement (or fusion) in an adaptive manner, using a validation set or cross-validation to estimate test set prediction error. In the setting of cooperative regularized linear regression, the method combines the lasso penalty with the agreement penalty (Ding, D., Li, S., Narasimhan, B., Tibshirani, R. (2021) <doi:10.1073/pnas.2202113119>).
	"""
	
	cran = "multiview" 

	version("0.8", md5="ab6e0d8b1452dbc73da4ab56bfb203fd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
