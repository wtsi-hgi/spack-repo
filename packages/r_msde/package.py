# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsde(RPackage):
	"""Bayesian Inference for Multivariate Stochastic Differential
Equations

	Implements an MCMC sampler for the posterior distribution of arbitrary time-homogeneous multivariate stochastic differential equation (SDE) models with possibly latent components.  The package provides a simple entry point to integrate user-defined models directly with the sampler's C++ code, and parallelizes large portions of the calculations when compiled with 'OpenMP'.
	"""
	
	cran = "msde" 

	version("1.0.5", md5="1db306b1fef1fc3bbb86ef05796aee29")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
