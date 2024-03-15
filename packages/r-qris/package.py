# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQris(RPackage):
	"""Quantile Regression Model for Residual Lifetime Using an Induced
Smoothing Approach

	A collection of functions is provided by this package to fit quantiles regression models for censored residual lifetimes. It provides various options for regression parameters estimation: the induced smoothing approach (smooth), and L1-minimization (non-smooth).  It also implements the estimation methods for standard errors of the regression parameters estimates based on an efficient partial multiplier bootstrap method and robust sandwich estimator. Furthermore, a simultaneous procedure of estimating regression parameters and their standard errors via an iterative updating procedure is implemented (iterative). For more details, see Kim, K. H., Caplan, D. J., & Kang, S. (2022), "Smoothed quantile regression for censored residual life", Computational Statistics, 1-22 <doi:10.1007/s00180-022-01262-z>.
	"""
	
	homepage = "https://github.com/Kyuhyun07/qris"
	cran = "qris" 

	version("1.1.1", md5="974e64d8ef2f130485972d6c3b9834e8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
