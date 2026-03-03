# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErgmito(RPackage):
	"""Exponential Random Graph Models for Small Networks

	Simulation and estimation of Exponential Random Graph Models (ERGMs)
  for small networks using exact statistics as shown in Vega Yon et al. (2020)
  <DOI:10.1016/j.socnet.2020.07.005>. As a difference from the 'ergm'
  package, 'ergmito' circumvents using Markov-Chain Maximum Likelihood Estimator
  (MC-MLE) and instead uses Maximum Likelihood Estimator (MLE) to fit ERGMs
  for small networks. As exhaustive enumeration is computationally feasible for
  small networks, this R package takes advantage of this and provides tools for
  calculating likelihood functions, and other relevant functions, directly,
  meaning that in many cases both estimation and simulation of ERGMs for
  small networks can be faster and more accurate than simulation-based
  algorithms.
	"""
	
	homepage = "https://muriteams.github.io/ergmito/"
	cran = "ergmito" 

	version("0.3-1", md5="11bf981dc890ba2f2566a480f6db9dbb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
