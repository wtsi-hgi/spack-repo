# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMstclustering(RPackage):
	""""MST-Based Clustering"

	Implements a minimum-spanning-tree-based heuristic for k-means clustering using a union-find disjoint set and the algorithm in Kruskal (1956) <doi:10.1090/S0002-9939-1956-0078686-7>.
	"""
	
	cran = "mstclustering" 

	version("1.0.0.0", md5="eb3924c57c54b6512abb9181f768d800")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
