# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiphynetwork(RPackage):
	"""A Phylogenetic Simulator for Reticulate Evolution

	A simulator for reticulate evolution under a birth-death-hybridization process. Here the birth-death process is extended to consider reticulate Evolution by allowing hybridization events to occur. The general purpose simulator allows the modeling of three different reticulate patterns: lineage generative hybridization, lineage neutral hybridization, and lineage degenerative hybridization. Users can also specify hybridization events to be dependent on a trait value or genetic distance. We also extend some phylogenetic tree utility and plotting functions for networks. We allow two different stopping conditions: simulated to a fixed time or number of taxa. When simulating to a fixed number of taxa, the user can simulate under the Generalized Sampling Approach that properly simulates phylogenies when assuming a uniform prior on the root age. 
	"""
	
	cran = "SiPhyNetwork" 

	version("1.1.0", md5="34c3c53eee530d1d865d2c50a30330d1")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rstackdeque", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
