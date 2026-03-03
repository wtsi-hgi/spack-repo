# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankaggreg(RPackage):
	"""Weighted Rank Aggregation

	Performs aggregation of ordered lists based
        on the ranks using several different algorithms:
        Cross-Entropy Monte Carlo algorithm, Genetic algorithm, and a
        brute force algorithm (for small problems).
	"""
	
	cran = "RankAggreg" 

	version("0.6.6", md5="2b54df8fd2b0097ec6aa80d607fd53a8")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
