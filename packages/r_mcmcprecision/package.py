# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcprecision(RPackage):
	"""Precision of Discrete Parameters in Transdimensional MCMC

	Estimates the precision of transdimensional Markov chain Monte Carlo 
    (MCMC) output, which is often used for Bayesian analysis of models with different 
    dimensionality (e.g., model selection). Transdimensional MCMC (e.g., reversible 
    jump MCMC) relies on sampling a discrete model-indicator variable to estimate 
    the posterior model probabilities. If only few switches occur between the models, 
    precision may be low and assessment based on the assumption of independent 
    samples misleading. Based on the observed transition matrix of the indicator 
    variable, the method of Heck, Overstall, Gronau, & Wagenmakers (2019, 
    Statistics & Computing, 29, 631-643) <doi:10.1007/s11222-018-9828-0> draws 
    posterior samples of the stationary distribution to (a) assess the uncertainty 
    in the estimated posterior model probabilities and (b) estimate the effective 
    sample size of the MCMC output.
	"""
	
	homepage = "https://github.com/danheck/MCMCprecision"
	cran = "MCMCprecision" 

	version("0.4.0", md5="856f4937cab0ed37f7b5c6108c43a077")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
