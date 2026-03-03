# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraven(RPackage):
	"""Bayes Nets: 'RHugin' Emulation with 'gRain'

	Wrappers for functions in the 'gRain' package to emulate some 'RHugin' 
  functionality, allowing the building of Bayesian networks consisting on discrete 
  chance nodes incrementally, through   adding nodes, edges and conditional probability 
  tables, the setting of evidence,   both 'hard' (boolean) or 'soft' (likelihoods), 
  querying marginal probabilities   and normalizing constants, and generating sets of
  high-probability configurations. Computations will typically not be so fast as they are
  with 'RHugin', but this package should assist users without access to 'Hugin' to use
  code written to use 'RHugin'.
	"""
	
	cran = "gRaven" 

	version("1.1.8", md5="070e77b66a408cbd516951123fddf1a0")

	depends_on("r-grain@1.3.12:", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
