# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaivereg(RPackage):
	"""Nonparametric Additive Instrumental Variable Estimator and
Related IV Methods

	In empirical studies, instrumental variable (IV) regression is the signature method to solve the endogeneity problem. If we enforce the exogeneity condition of the IV, it is likely that we end up with a large set of IVs without knowing which ones are good. Also, one could face the model uncertainty for structural equation, as large micro dataset is commonly available nowadays. This package uses adaptive group lasso and B-spline methods to select the nonparametric components of the IV function, with the linear function being a special case (naivereg). The package also incorporates two stage least squares estimator (2SLS), generalized method of moment (GMM), generalized empirical likelihood (GEL) methods post instrument selection, logistic-regression instrumental variables estimator (LIVE, for dummy endogenous variable problem), double-selection plus instrumental variable estimator (DS-IV) and double selection plus logistic regression instrumental variable estimator (DS-LIVE), where the double selection methods are useful for high-dimensional structural equation models. The naivereg is nonparametric version of 'ivregress' in 'Stata' with IV selection and high dimensional features. The package is based on the paper by Q. Fan and W. Zhong, "Nonparametric Additive Instrumental Variable Estimator: A Group Shrinkage Estimation Perspective" (2018), Journal of Business & Economic Statistics <doi:10.1080/07350015.2016.1180991> as well as a series of working papers led by the same authors. 
	"""
	
	cran = "naivereg" 

	version("1.0.5", md5="a6457788d49a600f64ec1359b788432d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
	depends_on("r-gmm", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
