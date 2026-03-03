# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlarma(RPackage):
	"""Generalized Linear Autoregressive Moving Average Models

	Functions are provided for estimation, testing, diagnostic checking and forecasting of generalized linear autoregressive moving average (GLARMA) models for discrete valued time series with regression variables.  These are a class of observation driven non-linear non-Gaussian state space models. The state vector consists of a linear regression component plus an observation driven component consisting of an autoregressive-moving average (ARMA) filter of past predictive residuals. Currently three distributions (Poisson, negative binomial and binomial) can be used for the response series. Three options (Pearson, score-type and unscaled) for the residuals in the observation driven component are available. Estimation is via maximum likelihood (conditional on initializing values for the ARMA process) optimized using Fisher scoring or Newton Raphson iterative methods. Likelihood ratio and Wald tests for the observation driven component allow testing for serial dependence in generalized linear model settings. Graphical diagnostics including model fits, autocorrelation functions and probability integral transform residuals are included in the package. Several standard data sets are included in the package.
	"""
	
	cran = "glarma" 

	version("1.6-0", md5="29d36b5cdd288bc29edfb0ab778db4eb")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
