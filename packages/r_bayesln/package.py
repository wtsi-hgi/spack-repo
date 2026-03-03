# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesln(RPackage):
	"""Bayesian Inference for Log-Normal Data

	Bayesian inference under log-normality assumption must be performed very carefully. In fact, under the common priors for the variance, useful quantities in the original data scale (like mean and quantiles) do not have posterior moments that are finite (Fabrizi et al. 2012 <doi:10.1214/12-BA733>). This package allows to easily carry out a proper Bayesian inferential procedure by fixing a suitable distribution (the generalized inverse Gaussian) as prior for the variance. Functions to estimate several kind of means (unconditional, conditional and conditional under a mixed model) and quantiles (unconditional and conditional) are provided. 
	"""
	
	cran = "BayesLN" 

	version("0.2.10", md5="9a9b80ff64d958b7b9a9848fc146f95b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-generalizedhyperbolic", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
