# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlm(RPackage):
	"""Stationary Linear Models

	Provides statistical procedures for linear regression in the general context where the errors are assumed to be correlated. Different ways to estimate the asymptotic covariance matrix of the least squares estimators are available. Starting from this estimation of the covariance matrix, the confidence intervals and the usual tests on the parameters are modified. The functions of this package are very similar to those of 'lm': it contains methods such as summary(), plot(), confint() and predict(). The 'slm' package is described in the paper by E. Caron, J. Dedecker and B. Michel (2019), "Linear regression with stationary errors: the R package slm", arXiv preprint <arXiv:1906.06583>.
	"""
	
	cran = "slm" 

	version("1.2.0", md5="d0f6d53a4992c648c49489bdb9eaa136")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ltsa", type=("build", "run"))
	depends_on("r-capushe", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
