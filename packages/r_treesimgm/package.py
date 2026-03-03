# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreesimgm(RPackage):
	"""Simulating Phylogenetic Trees under General Bellman Harris and
Lineage Shift Model

	Provides a flexible simulation tool for phylogenetic trees under a general model for speciation and extinction. Trees with a user-specified number of extant tips, or a user-specified stem age are simulated. It is possible to assume any probability distribution for the waiting time until speciation and extinction. Furthermore, the waiting times to speciation / extinction may be scaled in different parts of the tree, meaning we can simulate trees with clade-dependent diversification processes. At a speciation event, one species splits into two. We allow for two different modes at these splits: (i) symmetric, where for every speciation event new waiting times until speciation and extinction are drawn for both daughter lineages; and (ii) asymmetric, where a speciation event results in one species with new waiting times, and another that carries the extinction time and age of its ancestor. The symmetric mode can be seen as an vicariant or allopatric process where divided populations suffer equal evolutionary forces while the asymmetric mode could be seen as a peripatric speciation where a mother lineage continues to exist.  Reference: O. Hagen and T. Stadler (2017). TreeSimGM: Simulating phylogenetic trees under general Bellman Harris models with lineage-specific shifts of speciation and extinction in R. Methods in Ecology and Evolution. <doi:10.1111/2041-210X.12917>.
	"""
	
	cran = "TreeSimGM" 

	version("2.5", md5="e393b7251a1fb966e2a74af548d213c0")

	depends_on("r-treesim", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
