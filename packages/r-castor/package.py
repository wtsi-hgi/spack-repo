# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCastor(RPackage):
	"""Efficient Phylogenetics on Large Trees

	Efficient phylogenetic analyses on massive phylogenies comprising up to millions of tips. Functions include pruning, rerooting, calculation of most-recent common ancestors, calculating distances from the tree root and calculating pairwise distances. Calculation of phylogenetic signal and mean trait depth (trait conservatism), ancestral state reconstruction and hidden character prediction of discrete characters, simulating and fitting models of trait evolution, fitting and simulating diversification models, dating trees, comparing trees, and reading/writing trees in Newick format. Citation: Louca, Stilianos and Doebeli, Michael (2017) <doi:10.1093/bioinformatics/btx701>.
	"""
	
	cran = "castor" 

	version("1.8.0", md5="b240641eb72d741cf7bb9675de9572b3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-naturalsort", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
