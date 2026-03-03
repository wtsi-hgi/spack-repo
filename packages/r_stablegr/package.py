# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStablegr(RPackage):
	"""A Stable Gelman-Rubin Diagnostic for Markov Chain Monte Carlo

	Practitioners of Bayesian statistics often use Markov chain Monte Carlo (MCMC) samplers to sample from a posterior distribution. This package determines whether the MCMC sample is large enough   to yield reliable estimates of the target distribution. In particular, this calculates a Gelman-Rubin convergence diagnostic using stable and consistent estimators of Monte Carlo variance. Additionally, this uses the connection between an MCMC sample's effective sample size and the Gelman-Rubin diagnostic to produce a threshold for terminating MCMC simulation. Finally, this informs the user whether enough samples have been collected  and (if necessary) estimates the number of samples needed for a desired level of accuracy. The theory underlying these methods can be found in "Revisiting the Gelman-Rubin Diagnostic" by Vats and  Knudson (2018) <arXiv:1812:09384>. 
	"""
	
	cran = "stableGR" 

	version("1.2", md5="5fa60a62e86e5a1ff0e1f4ee8895abb3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mcmcse@1.4.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
