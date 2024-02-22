# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesdistreg(RPackage):
	"""Bayesian Distribution Regression

	Implements Bayesian Distribution Regression methods. This package contains functions for three estimators (non-asymptotic, semi-asymptotic and asymptotic) and related routines for Bayesian Distribution Regression in Huang and Tsyawo (2018) <doi:10.2139/ssrn.3048658> which is also the recommended reference to cite for this package. The functions can be grouped into three (3) categories. The first computes the logit likelihood function and posterior densities under uniform and normal priors. The second contains Independence and Random Walk Metropolis-Hastings Markov Chain Monte Carlo (MCMC) algorithms as functions and the third category of functions are useful for semi-asymptotic and asymptotic Bayesian distribution regression inference.
	"""
	
	cran = "bayesdistreg" 

	version("0.1.0", md5="fd6cda65adc6d8b8cd07a7c0379d7aa0")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
