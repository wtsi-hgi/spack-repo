# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobsa(RPackage):
	"""Robust Bayesian Survival Analysis

	A framework for estimating ensembles of parametric survival models
    with different parametric families. The RoBSA framework uses Bayesian 
    model-averaging to combine the competing parametric survival models into 
    a model ensemble, weights the posterior parameter distributions based on 
    posterior model probabilities and uses Bayes factors to test for the 
    presence or absence of the individual predictors or preference for a 
    parametric family (Bartoš, Aust & Haaf, 2022, <doi:10.1186/s12874-022-01676-9>).
    The user can define a wide range of informative priors for all parameters 
    of interest. The package provides convenient functions for summary, visualizations, 
    fit diagnostics, and prior distribution calibration.
	"""
	
	homepage = "https://fbartos.github.io/RoBSA/"
	cran = "RoBSA" 

	version("1.0.2", md5="a53485ac46d0c60cba91c2520b93ad9a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bayestools@0.2.14:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("jags@4.3.1:", type=("build", "link", "run"))
