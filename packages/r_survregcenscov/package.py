# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvregcenscov(RPackage):
	"""Weibull Regression for a Right-Censored Endpoint with
Interval-Censored Covariate

	The function SurvRegCens() of this package allows estimation of a Weibull Regression for a right-censored endpoint, one interval-censored covariate, and an arbitrary number of non-censored covariates. Additional functions allow to switch between different parametrizations of Weibull regression used by different R functions, inference for the mean difference of two arbitrarily censored Normal samples, and estimation of canonical parameters from censored samples for several distributional assumptions. Hubeaux, S. and Rufibach, K. (2014) <arXiv:1402.0432>.
	"""
	
	cran = "SurvRegCensCov" 

	version("1.7", md5="25f9b7e5ddce7737d04b929d4ad9782f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
