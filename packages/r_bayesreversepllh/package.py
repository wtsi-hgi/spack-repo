# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesreversepllh(RPackage):
	"""Fits the Bayesian Piecewise Linear Log-Hazard Model

	Contains posterior samplers for the Bayesian piecewise linear log-hazard and piecewise exponential hazard models, including Cox models. Posterior mean restricted survival times are also computed for non-Cox an Cox models with only treatment indicators. The ApproxMean() function can be used to estimate restricted posterior mean survival times given a vector of patient covariates in the Cox model. Functions included to return the posterior mean hazard and survival functions for the piecewise exponential and piecewise linear log-hazard models. Chapple, AG, Peak, T, Hemal, A (2020). Under Revision.
	"""
	
	cran = "BayesReversePLLH" 

	version("1.5", md5="44ca3b9f87ad0d6692a3130d71f62b84")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
