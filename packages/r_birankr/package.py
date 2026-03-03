# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBirankr(RPackage):
	"""Ranking Nodes in Bipartite and Weighted Networks

	Highly efficient functions for estimating various rank (centrality) measures of nodes in bipartite graphs (two-mode networks). Includes methods for estimating HITS, CoHITS, BGRM, and BiRank with implementation primarily inspired by He et al. (2016) <doi:10.1109/TKDE.2016.2611584>. Also provides easy-to-use tools for efficiently estimating PageRank in one-mode graphs, incorporating or removing edge-weights during rank estimation, projecting two-mode graphs to one-mode, and for converting edgelists and matrices to sparseMatrix format. Best of all, the package's rank estimators can work directly with common formats of network data including edgelists (class data.frame, data.table, or tbl_df) and adjacency matrices (class matrix or dgCMatrix).
	"""
	
	cran = "birankr" 

	version("1.0.1", md5="3a1e86c39d8c0004878b7bd2a2498f61")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
