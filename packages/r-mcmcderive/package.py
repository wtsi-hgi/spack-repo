# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcderive(RPackage):
	"""Derive MCMC Parameters

	Generates derived parameter(s) from Monte Carlo Markov Chain
    (MCMC) samples using R code. This allows Bayesian models to be fitted
    without the inclusion of derived parameters which add unnecessary
    clutter and slow model fitting. For more information on MCMC samples
    see Brooks et al. (2011) <isbn:978-1-4200-7941-8>.
	"""
	
	homepage = "https://github.com/poissonconsulting/mcmcderive"
	cran = "mcmcderive" 

	version("0.1.2", md5="e331664275efbb7bafa86930f62aab0b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-extras", type=("build", "run"))
	depends_on("r-mcmcr", type=("build", "run"))
	depends_on("r-nlist", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-universals", type=("build", "run"))
