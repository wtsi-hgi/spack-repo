# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRunmcmcbtadjust(RPackage):
	"""Runs Monte Carlo Markov Chain - With Either 'JAGS', 'nimble' or
'greta' - While Adjusting Burn-in and Thinning Parameters

	The function runMCMC_btadjust() returns a mcmc.list object which is the output of a 
  Markov Chain Monte Carlo obtained - from either 'JAGS', 'nimble' or 'greta' - after adjusting burn-in and thinning parameters to meet 
  pre-specified criteria in terms of convergence & effective sample size.
	"""
	
	cran = "runMCMCbtadjust" 

	version("1.0.5", md5="b29f620e12cfed9b3d90826c3b4cdee3")

	depends_on("r-coda", type=("build", "run"))
