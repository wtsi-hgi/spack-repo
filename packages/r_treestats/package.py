# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreestats(RPackage):
	"""Phylogenetic Tree Statistics

	Collection of phylogenetic tree statistics,
             collected throughout the literature. All functions have been 
             written to maximize computation speed. The package includes 
             umbrella functions to calculate all statistics, all balance 
             associated statistics, or all branching time related statistics. 
             Furthermore, the 'treestats' package supports summary statistic 
             calculations on Ltables, provides speed-improved coding of 
             branching times, Ltable conversion and includes algorithms to
             create intermediately balanced trees. Full description can be
             found in Janzen (2023) <doi:10.1101/2024.01.24.576848>.
	"""
	
	homepage = "https://github.com/thijsjanzen/treestats"
	cran = "treestats" 

	version("1.0.5", md5="5aa759c4c69e76bee91062194fdfb061")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
