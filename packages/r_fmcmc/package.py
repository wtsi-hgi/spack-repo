# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmcmc(RPackage):
	"""A friendly MCMC framework

	Provides a friendly (flexible) Markov Chain Monte Carlo (MCMC)
         framework for implementing Metropolis-Hastings algorithm in a modular way
         allowing users to specify automatic convergence checker, personalized
         transition kernels, and out-of-the-box multiple MCMC chains using
         parallel computing. Most of the methods implemented in this package can
         be found in Brooks et al. (2011, ISBN 9781420079425). Among the methods
         included, we have: Haario (2001) <doi:10.1007/s11222-011-9269-5>
         Adaptive Metropolis, Vihola (2012) <doi:10.1007/s11222-011-9269-5>
         Robust Adaptive Metropolis, and Thawornwattana et
         al. (2018) <doi:10.1214/17-BA1084> Mirror transition kernels.
	"""
	
	homepage = "https://github.com/USCbiostats/fmcmc"
	cran = "fmcmc" 

	version("0.5-2", md5="acddf457668983d96da04a20cba7d7d5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
