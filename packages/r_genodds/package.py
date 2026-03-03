# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenodds(RPackage):
	"""Generalised Odds Ratios

	
  Calculates Agresti's generalized odds ratios.
  For a randomly selected pair of observations
  from two groups, calculates the odds that
  the second group will have a higher scoring outcome
  than that of the first group.
  Package provides hypothesis testing for if this odds
  ratio is significantly different to 1 (equal chance).
	"""
	
	cran = "genodds" 

	version("1.1.2", md5="486d96ff951248c255924507a35253d8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
