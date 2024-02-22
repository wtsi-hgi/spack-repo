# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactorstochvol(RPackage):
	"""Bayesian Estimation of (Sparse) Latent Factor Stochastic
Volatility Models

	Markov chain Monte Carlo (MCMC) sampler for fully Bayesian estimation of latent factor stochastic volatility models with interweaving <doi:10.1080/10618600.2017.1322091>. Sparsity can be achieved through the usage of Normal-Gamma priors on the factor loading matrix <doi:10.1016/j.jeconom.2018.11.007>.
	"""
	
	cran = "factorstochvol" 

	version("1.1.0", md5="43cb6a965bdcc526dc85d5726fb64f7c")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-gigrvg@0.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-stochvol", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.900:", type=("build", "run"))
