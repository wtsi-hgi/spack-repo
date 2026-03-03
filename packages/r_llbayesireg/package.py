# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLlbayesireg(RPackage):
	"""The L-Logistic Bayesian Regression

	R functions and data sets for the work Paz, R.F., Balakrishnan, N and Bazán, J.L. (2018). L-logistic regression models: Prior sensitivity analysis, robustness to outliers and applications. Brazilian Journal of Probability and Statistics, <https://www.imstat.org/wp-content/uploads/2018/05/BJPS397.pdf>. 
	"""
	
	cran = "llbayesireg" 

	version("1.0.0", md5="a62e190a48a44242673e9eba70f491c0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-llogistic", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
