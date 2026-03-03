# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesforecast(RPackage):
	"""Bayesian Time Series Modeling with Stan

	Fit Bayesian time series models using 'Stan' for full Bayesian inference. A wide range 
  of distributions and models are supported, allowing users to fit Seasonal ARIMA, ARIMAX, Dynamic 
  Harmonic Regression, GARCH, t-student innovation GARCH models, asymmetric GARCH, Random Walks, stochastic 
  volatility models for univariate time series.  Prior specifications are flexible and explicitly encourage 
  users to apply prior distributions that actually reflect their beliefs. Model fit can easily be assessed 
  and compared with typical visualization methods, information criteria such as loglik, AIC, BIC WAIC, Bayes 
  factor and leave-one-out cross-validation methods. References: Hyndman (2017)
    <doi:10.18637/jss.v027.i03>; Carpenter et al. (2017) <doi:10.18637/jss.v076.i01>.
	"""
	
	cran = "bayesforecast" 

	version("1.0.1", md5="5046737b4171308581264c63f732b492")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bayesplot@1.5:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-loo@2.2:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-bridgesampling@0.3.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-astsa", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-prophet", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
