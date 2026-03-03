# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchaeochron(RPackage):
	"""Bayesian Modeling of Archaeological Chronologies

	Provides a list of functions for the Bayesian modeling of archaeological chronologies. The Bayesian models are implemented in 'JAGS' ('JAGS' stands for Just Another Gibbs Sampler. It is a program for the analysis of Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC) simulation. See <http://mcmc-jags.sourceforge.net/> and "JAGS Version 4.3.0 user manual", Martin Plummer (2017) <https://sourceforge.net/projects/mcmc-jags/files/Manuals/>.). The inputs are measurements with their associated standard deviations and the study period. The output is the MCMC sample of the posterior distribution of the event date with or without radiocarbon calibration. 
	"""
	
	cran = "ArchaeoChron" 

	version("0.1", md5="9c99d41a7ca7032a93e993ceaedf3a6a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-archaeophases", type=("build", "run"))
	depends_on("r-bchron", type=("build", "run"))
