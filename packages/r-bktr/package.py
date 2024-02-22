# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBktr(RPackage):
	"""Bayesian Kernelized Tensor Regression

	Facilitates scalable spatiotemporally varying coefficient
    modelling with Bayesian kernelized tensor regression.
    The important features of this package are:
    (a) Enabling local temporal and spatial modeling of the relationship between
    the response variable and covariates.
    (b) Implementing the model described by Lei et al. (2023) <doi:10.48550/arXiv.2109.00046>.
    (c) Using a Bayesian Markov Chain Monte Carlo (MCMC) algorithm to sample from the posterior
    distribution of the model parameters.
    (d) Employing a tensor decomposition to reduce the number of estimated parameters.
    (e) Accelerating tensor operations and enabling graphics processing unit (GPU) acceleration
    with the 'torch' package.
	"""
	
	cran = "BKTR" 

	version("0.1.1", md5="7b57ffa345ba396f8db4cc0b9fc1e6f5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-r6p", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
