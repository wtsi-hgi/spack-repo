# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppcensspatial(RPackage):
	"""Spatial Estimation and Prediction for Censored/Missing Responses

	It provides functions to estimate parameters in linear spatial models with 
  censored/missing responses via the Expectation-Maximization (EM), the Stochastic 
  Approximation EM (SAEM), or the Monte Carlo EM (MCEM) algorithm. These algorithms 
  are widely used to compute the maximum likelihood (ML) estimates in problems with 
  incomplete data. The EM algorithm computes the ML estimates when a closed expression 
  for the conditional expectation of the complete-data log-likelihood function is 
  available. In the MCEM algorithm, the conditional expectation is substituted by a 
  Monte Carlo approximation based on many independent simulations of the missing data. 
  In contrast, the SAEM algorithm splits the E-step into simulation and integration 
  steps. This package also approximates the standard error of the estimates using the 
  Louis method. Moreover, it has a function that performs spatial prediction in new 
  locations.
	"""
	
	cran = "RcppCensSpatial" 

	version("0.3.0", md5="0f0493a09762f3d66ffa3ade6c16f36b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-momtrunc", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-relliptical", type=("build", "run"))
	depends_on("r-stempcens", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-roptim", type=("build", "run"))
