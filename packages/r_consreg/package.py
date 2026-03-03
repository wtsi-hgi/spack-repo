# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsreg(RPackage):
	"""Fits Regression & ARMA Models Subject to Constraints to the
Coefficient

	Fits or generalized linear models either a regression with Autoregressive moving-average (ARMA) errors for time series data. 
       The package makes it easy to incorporate constraints into the model's coefficients. 
          The model is specified by an objective function (Gaussian, Binomial or Poisson) or an ARMA order (p,q), 
          a vector of bound constraints 
          for the coefficients (i.e beta1 > 0) and the possibility to incorporate restrictions
          among coefficients (i.e beta1 > beta2).
          The references of this packages are the same as 'stats' package for glm() and arima() functions.
          See Brockwell, P. J. and Davis, R. A. (1996, ISBN-10: 9783319298528).
          For the different optimizers implemented, it is recommended to consult the documentation of the corresponding packages. 
	"""
	
	homepage = "https://github.com/puigjos/ConsReg"
	cran = "ConsReg" 

	version("0.1.0", md5="5f8ac16cd094cefc1585be7fd9c323be")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-forecast@8:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-nloptr@1.2:", type=("build", "run"))
	depends_on("r-fme@1.3:", type=("build", "run"))
	depends_on("r-mcmcpack@1.4:", type=("build", "run"))
	depends_on("r-rsolnp@1.15:", type=("build", "run"))
	depends_on("r-deoptim@2.2:", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-ga@3:", type=("build", "run"))
	depends_on("r-gensa@1.1:", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-adaptmcmc", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
