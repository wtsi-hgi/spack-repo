# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSebr(RPackage):
	"""Semiparametric Bayesian Regression Analysis

	Monte Carlo and MCMC sampling algorithms for semiparametric
    Bayesian regression analysis. These models feature a nonparametric
    (unknown) transformation of the data paired with widely-used
    regression models including linear regression, spline regression,
    quantile regression, and Gaussian processes. The transformation
    enables broader applicability of these key models, including for
    real-valued, positive, and compactly-supported data with challenging
    distributional features. The samplers prioritize computational
    scalability and, for most cases, Monte Carlo (not MCMC) sampling for
    greater efficiency. Details of the methods and algorithms are provided
    in Kowal and Wu (2023) <arXiv:2306.05498>.
	"""
	
	homepage = "https://github.com/drkowal/SeBR"
	cran = "SeBR" 

	version("1.0.0", md5="a93a181729aa14a8cf6a72caab7153bf")

	depends_on("r-fields", type=("build", "run"))
	depends_on("r-gpgp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-spikeslabgam", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
