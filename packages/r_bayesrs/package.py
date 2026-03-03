# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesrs(RPackage):
	"""Bayes Factors for Hierarchical Linear Models with Continuous
Predictors

	Runs hierarchical linear Bayesian models. Samples from the posterior
    distributions of model parameters in JAGS (Just Another Gibbs Sampler;
	Plummer, 2017, <http://mcmc-jags.sourceforge.net>). Computes Bayes factors for group
	parameters of interest with the Savage-Dickey density ratio (Wetzels,
	Raaijmakers, Jakab, Wagenmakers, 2009, <doi:10.3758/PBR.16.4.752>).
	"""
	
	cran = "BayesRS" 

	version("0.1.3", md5="422d8f534a087d153ff4bdd73878f62a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metrology", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
