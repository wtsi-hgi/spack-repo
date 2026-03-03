# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayeszib(RPackage):
	"""Bayesian Zero-Inflated Bernoulli Regression Model

	Fits a Bayesian zero-inflated Bernoulli regression model handling (potentially) different covariates for the zero-inflated
    and non zero-inflated parts. See Moriña D, Puig P, Navarro A. (2021) <doi:10.1186/s12874-021-01427-2>.
	"""
	
	cran = "bayesZIB" 

	version("0.0.5", md5="7948caae15b0262f0ebcd55217495194")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
