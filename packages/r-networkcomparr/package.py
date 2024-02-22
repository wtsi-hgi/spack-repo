# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkcomparr(RPackage):
	"""Statistical Comparison of Networks

	A permutation-based hypothesis test for statistical comparison of two networks based on the invariance measures of the R package 'NetworkComparisonTest' by van Borkulo et al. (2022), <doi:10.1037/met0000476>: network structure invariance, global strength invariance, edge invariance, and various centrality measures. Edgelists from dependent or independent samples are used as input. These edgelists are generated from concept maps and summed into two comparable group networks. The networks can be directed or undirected.
	"""
	
	cran = "NetworkComparr" 

	version("0.0.0.9", md5="c47e72d709fa5db006086d786fdbbc51")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-networktools", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
