# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetcmc(RPackage):
	"""Spatio-Network Generalised Linear Mixed Models for Areal Unit
and Network Data

	Implements a class of univariate and multivariate spatio-network generalised linear mixed models for areal unit and network data, with inference in a Bayesian setting using Markov chain Monte Carlo (MCMC) simulation. The response variable can be binomial, Gaussian, or Poisson. Spatial autocorrelation is modelled by a set of random effects that are assigned a conditional autoregressive (CAR) prior distribution following the Leroux model (Leroux et al. (2000) <doi:10.1007/978-1-4612-1284-3_4>). Network structures are modelled by a set of random effects that reflect a multiple membership structure (Browne et al. (2001) <doi:10.1177/1471082X0100100202>).
	"""
	
	cran = "netcmc" 

	version("1.0.2", md5="dca2925573f1b03a5e59cb88dc978179")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
