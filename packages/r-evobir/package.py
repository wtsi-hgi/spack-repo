# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvobir(RPackage):
	"""Comparative and Population Genetic Analyses

	Comparative analysis of continuous traits influencing discrete states, and utility tools to facilitate comparative analyses.  Implementations of ABBA/BABA type statistics to test for introgression in genomic data. Wright-Fisher, phylogenetic tree, and statistical distribution Shiny interactive simulations for use in teaching.
	"""
	
	homepage = "http://www.uta.edu/karyodb/evobiR/"
	cran = "evobiR" 

	version("1.1", md5="e40f2a6716ac04c7f15cd3041bdbe153")

	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
