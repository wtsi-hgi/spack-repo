# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSteepness(RPackage):
	"""Testing Steepness of Dominance Hierarchies

	The steepness package computes steepness as a
        property of dominance hierarchies. Steepness is defined as the
        absolute slope of the straight line fitted to the normalized
        David's scores. The normalized David's scores can be obtained
        on the basis of dyadic dominance indices corrected for chance
        or by means of proportions of wins. Given an observed
        sociomatrix, it computes hierarchy's steepness and estimates
        statistical significance by means of a randomization test.
	"""
	
	cran = "steepness" 

	version("0.3-0", md5="37411cd820b5924646f78fe98c6edb79")

	depends_on("r@4.1:", type=("build", "run"))
