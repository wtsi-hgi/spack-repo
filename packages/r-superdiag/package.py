# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperdiag(RPackage):
	"""A Comprehensive Test Suite for Testing Markov Chain
Nonconvergence

	The 'superdiag' package provides a comprehensive test suite for testing
  Markov Chain nonconvergence. It integrates five standard empirical MCMC convergence
  diagnostics (Gelman-Rubin, Geweke, Heidelberger-Welch, Raftery-Lewis, and Hellinger
  distance) and plotting functions for trace plots and density histograms. The functions
  of the package can be used to present all diagnostic statistics and graphs at once
  for conveniently checking MCMC nonconvergence.
	"""
	
	cran = "superdiag" 

	version("2.0", md5="719b4e85c00b4bb47acae5e18b193f4f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
