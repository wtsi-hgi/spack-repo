# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustcomp(RPackage):
	"""Clustering Comparison Package

	clustComp is a package that implements several techniques for the comparison and visualisation of relationships between different clustering results, either flat versus flat or hierarchical versus flat. These relationships among clusters are displayed using a weighted bi-graph, in which the nodes represent the clusters and the edges connect pairs of nodes with non-empty intersection; the weight of each edge is the number of elements in that intersection and is displayed through the edge thickness. The best layout of the bi-graph is provided by the barycentre algorithm, which minimises the weighted number of crossings. In the case of comparing a hierarchical and a non-hierarchical clustering, the dendrogram is pruned at different heights, selected by exploring the tree by depth-first search, starting at the root. Branches are decided to be split according to the value of a scoring function, that can be based either on the aesthetics of the bi-graph or on the mutual information between the hierarchical and the flat clusterings. A mapping between groups of clusters from each side is constructed with a greedy algorithm, and can be additionally visualised.
	"""
	
	bioc = "clustComp" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/clustComp_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/clustComp/clustComp_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="a53c4f1b22ecb2a2cb4dd50327b23f58eab48c619925a45a53de3f8cc2449dcb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
