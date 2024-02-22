# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtras(RPackage):
	"""Helper Functions for Bayesian Analyses

	Functions to 'numericise' 'R' objects (coerce to numeric
    objects), summarise 'MCMC' (Monte Carlo Markov Chain) samples and
    calculate deviance residuals as well as 'R' translations of some
    'BUGS' (Bayesian Using Gibbs Sampling), 'JAGS' (Just Another Gibbs
    Sampler), 'STAN' and 'TMB' (Template Model Builder) functions.
	"""
	
	homepage = "https://poissonconsulting.github.io/extras/"
	cran = "extras" 

	version("0.6.1", md5="763ea3ed6f4a9145fa1b0e1b7299358f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
