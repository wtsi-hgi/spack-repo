# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNode2vec(RPackage):
	"""Algorithmic Framework for Representational Learning on Graphs

	Given any graph, the 'node2vec' algorithm can learn continuous feature representations for the nodes, which can then be used for various downstream machine learning tasks.The techniques are detailed in the paper "node2vec: Scalable Feature Learning for Networks" by Aditya Grover, Jure Leskovec(2016),available at <arXiv:1607.00653>.
	"""
	
	cran = "node2vec" 

	version("0.1.0", md5="42953c0121b9cf52d719547fed920153")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-word2vec", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
