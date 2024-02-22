# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQris(RPackage):
	"""Quantile Regression Model for Residual Lifetime Using an Induced
Smoothing Approach

	A collection of functions to fit quantiles regression models for censored residual lifetimes. It provides various options for regression parameters estimation: the induced smoothing approach (smooth), and L1-minimization (non-smooth).  It also implements the estimation methods for standard errors of the regression parameters estimates based on an efficient partial multiplier bootstrap method and robust sandwich estimator. Furthermore, a simultaneous procedure of estimating regression parameters and their standard errors via an iterative updating procedure is implemented (iterative). See Kim, K. (2022) "Smoothed quantile regression for censored residual life", <arXiv:2205.00413>.
	"""
	
	homepage = "https://github.com/Kyuhyun07/qris"
	cran = "qris" 

	version("1.0.0", md5="1c1fa875f8d0cd8ffe31c39dfced0088")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
