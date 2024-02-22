# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgw(RPackage):
	"""Bayesian Survival Model with Lasso Shrinkage Using Generalized
Weibull Regression

	Bayesian survival model using Weibull regression on both scale and shape parameters. Dependence of shape parameter on covariates permits deviation from proportional-hazard assumption, leading to dynamic - i.e. non-constant with time - hazard ratios between subjects. Bayesian Lasso shrinkage in the form of two Laplace priors - one for scale and one for shape coefficients - allows for many covariates to be included. Cross-validation helper functions can be used to tune the shrinkage parameters. Monte Carlo Markov Chain (MCMC) sampling using a Gibbs wrapper around Radford Neal's univariate slice sampler (R package MfUSampler) is used for coefficient estimation.
	"""
	
	cran = "BSGW" 

	version("0.9.4", md5="8b9dc31b02e727318d472cbd6e6c51b8")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mfusampler", type=("build", "run"))
