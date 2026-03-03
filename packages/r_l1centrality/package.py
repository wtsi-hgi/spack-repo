# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL1centrality(RPackage):
	"""Graph/Network Analysis Based on L1 Centrality

	Analyze graph/network data using L1 centrality. Functions for deriving global and local L1 centrality and L1 centrality-based neighborhoods of vertices are provided. Routines for visual inspection of a graph/network are also provided.
	"""
	
	homepage = "https://github.com/seungwoo-stat/L1centrality"
	cran = "L1centrality" 

	version("0.0.3", md5="5a6bd3c892aa5b6aa71ced70b336c4c0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
