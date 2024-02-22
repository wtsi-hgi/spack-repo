# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrmest(RPackage):
	"""Different Types of Estimators to Deal with Multicollinearity

	When multicollinearity exists among predictor variables of the linear model, least square estimators does not provide a better solution for estimating parameters. To deal with multicollinearity several estimators are proposed in the literature. Some of these estimators are Ordinary Least Square Estimator (OLSE), Ordinary Generalized Ordinary Least Square Estimator (OGOLSE), Ordinary Ridge Regression Estimator (ORRE), Ordinary Generalized Ridge Regression Estimator (OGRRE), Restricted Least Square Estimator (RLSE), Ordinary Generalized Restricted Least Square Estimator (OGRLSE), Ordinary Mixed Regression Estimator (OMRE), Ordinary Generalized Mixed Regression Estimator (OGMRE), Liu Estimator (LE), Ordinary Generalized Liu Estimator (OGLE), Restricted Liu Estimator (RLE), Ordinary Generalized Restricted Liu Estimator (OGRLE), Stochastic Restricted Liu Estimator (SRLE), Ordinary Generalized Stochastic Restricted Liu Estimator (OGSRLE), Type (1),(2),(3) Liu Estimator (Type-1,2,3 LTE), Ordinary Generalized Type (1),(2),(3) Liu Estimator (Type-1,2,3 OGLTE), Type (1),(2),(3) Adjusted Liu Estimator (Type-1,2,3 ALTE), Ordinary Generalized Type (1),(2),(3) Adjusted Liu Estimator (Type-1,2,3 OGALTE), Almost Unbiased Ridge Estimator (AURE), Ordinary Generalized Almost Unbiased Ridge Estimator (OGAURE), Almost Unbiased Liu Estimator (AULE), Ordinary Generalized Almost Unbiased Liu Estimator (OGAULE), Stochastic Restricted Ridge Estimator (SRRE), Ordinary Generalized Stochastic Restricted Ridge Estimator (OGSRRE), Restricted Ridge Regression Estimator (RRRE) and Ordinary Generalized Restricted Ridge Regression Estimator (OGRRRE). To select the best estimator in a practical situation the Mean Square Error (MSE) is used. Using this package scalar MSE value of all the above estimators and Prediction Sum of Square (PRESS) values of some of the estimators can be obtained, and the variation of the MSE and PRESS values for the relevant estimators can be shown graphically. 
	"""
	
	cran = "lrmest" 

	version("3.0", md5="86c8214bfb3147225c82607b13ef5d8a")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
