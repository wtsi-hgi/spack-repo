# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REntropymcmc(RPackage):
	"""MCMC Simulation and Convergence Evaluation using Entropy and
Kullback-Leibler Divergence Estimation

	Tools for Markov Chain Monte Carlo (MCMC) simulation and performance analysis. Simulate MCMC algorithms including adaptive MCMC, evaluate their convergence rate, and compare candidate MCMC algorithms for a same target density, based on entropy and Kullback-Leibler divergence criteria. MCMC algorithms can be simulated using provided functions, or imported from external codes. This package is based upon work starting with Chauveau, D. and Vandekerkhove, P. (2013) <doi:10.1051/ps/2012004> and next articles.
	"""
	
	cran = "EntropyMCMC" 

	version("1.0.4", md5="ea825d70f62493a3643e9b2e9a4d952e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
