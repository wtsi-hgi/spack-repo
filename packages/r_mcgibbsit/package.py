# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcgibbsit(RPackage):
	"""Warnes and Raftery's 'MCGibbsit' MCMC Run Length and Convergence
Diagnostic

	
  Implementation of Warnes & Raftery's MCGibbsit run-length and 
  convergence diagnostic for a set of (not-necessarily independent) 
  Markov Chain Monte Carlo (MCMC) samplers.  It combines the quantile 
  estimate error-bounding approach of the Raftery and Lewis MCMC run
  length diagnostic `gibbsit` with the between verses within chain 
  approach of the Gelman and Rubin MCMC convergence diagnostic.
	"""
	
	homepage = "https://github.com/r-gregmisc/mcgibbsit"
	cran = "mcgibbsit" 

	version("1.2.2", md5="ffe9a94ba8d1312c971e6aecf80e9c79")

	depends_on("r-coda", type=("build", "run"))
