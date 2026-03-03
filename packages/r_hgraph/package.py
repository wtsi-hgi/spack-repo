# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgraph(RPackage):
	"""Use Graph Structure to Travel

	It is used to travel graphs, by using DFS and BFS to get the path from node to each leaf node.
  Depth first traversal(DFS) is a recursive algorithm for searching all the vertices of a graph or tree data structure.
  Traversal means visiting all the nodes of a graph.
  Breadth first traversal(BFS) algorithm is used to search a tree or graph data structure for a node that meets a set of criteria.
  It starts at the tree’s root or graph and searches/visits all nodes at the current depth level before moving on to the nodes at the next depth level.
  Also, it provides the matrix which is reachable between each node.
  Implement reference about Baruch Awerbuch (1985) <doi:10.1016/0020-0190(85)90083-3>.
	"""
	
	cran = "HGraph" 

	version("0.1.0", md5="a3eefbd6b0c06b876f05a8b1e4c3b5b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
