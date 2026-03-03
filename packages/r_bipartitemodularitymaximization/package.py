# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBipartitemodularitymaximization(RPackage):
	"""Partition Bipartite Network into Non-Overlapping Biclusters by
Optimizing Bipartite Modularity

	Function bipmod() that partitions a bipartite network into non-overlapping biclusters by maximizing bipartite modularity defined in Barber (2007) <doi:10.1103/PhysRevE.76.066102> using the bipartite version of the algorithm described in Treviño (2015) <doi:10.1088/1742-5468/2015/02/P02003>. 
	"""
	
	cran = "BipartiteModularityMaximization" 

	version("1.23.120.1", md5="812f787366a1975e14b7eca20872bfbc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
