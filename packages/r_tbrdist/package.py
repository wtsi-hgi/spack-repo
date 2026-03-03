# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbrdist(RPackage):
	"""Rearrangement Distances Between Unrooted Phylogenetic Trees

	Fast calculation of the Subtree Prune and Regraft (SPR),
  Tree Bisection and Reconnection (TBR) and Replug distances between 
  unrooted trees, using the algorithms of Whidden and 
  Matsen (2017) <arxiv:1511.07529>.
	"""
	
	homepage = "https://ms609.github.io/TBRDist/"
	cran = "TBRDist" 

	version("1.0.2", md5="7a06099570b709d23bba2ffc586f7ffc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-treedist", type=("build", "run"))
	depends_on("r-treetools@1.1:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
