# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoral(RPackage):
	"""Bayesian Ordination and Regression AnaLysis

	Bayesian approaches for analyzing multivariate data in ecology. Estimation is performed using Markov Chain Monte Carlo (MCMC) methods via Three. JAGS types of models may be fitted: 1) With explanatory variables only, boral fits independent column Generalized Linear Models (GLMs) to each column of the response matrix; 2) With latent variables only, boral fits a purely latent variable model for model-based unconstrained ordination; 3) With explanatory and latent variables, boral fits correlated column GLMs with latent variables to account for any residual correlation between the columns of the response matrix. 
	"""
	
	cran = "boral" 

	version("2.0", md5="6745c5818c637a9f176143a64a0eec77")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-fishmod", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
