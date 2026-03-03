# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJagsui(RPackage):
	"""A Wrapper Around 'rjags' to Streamline 'JAGS' Analyses

	A set of wrappers around 'rjags' functions to run Bayesian analyses in 'JAGS' (specifically, via 'libjags').  A single function call can control adaptive, burn-in, and sampling MCMC phases, with MCMC chains run in sequence or in parallel. Posterior distributions are automatically summarized (with the ability to exclude some monitored nodes if desired) and functions are available to generate figures based on the posteriors (e.g., predictive check plots, traceplots). Function inputs, argument syntax, and output format are nearly identical to the 'R2WinBUGS'/'R2OpenBUGS' packages to allow easy switching between MCMC samplers.
	"""
	
	homepage = "https://kenkellner.com/jagsUI/"
	cran = "jagsUI" 

	version("1.6.2", md5="3422a68f727c27259a6e74e5a8723aa5")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-coda@0.13:", type=("build", "run"))
	depends_on("r-rjags@3.13:", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
