# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworklite(RPackage):
	"""An Simplified Implementation of the 'network' Package
Functionality

	An implementation of some of the core 'network' package functionality based on a 
    simplified data structure that is faster in many research applications. This package is designed 
    for back-end use in the 'statnet' family of packages, including 'EpiModel'. Support is provided for
    binary and weighted, directed and undirected, bipartite and unipartite networks; no current 
    support for multigraphs, hypergraphs, or loops.
	"""
	
	homepage = "https://github.com/EpiModel/networkLite/"
	cran = "networkLite" 

	version("1.0.5", md5="9a93fd3d5bef7bc026713ff67696950c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-network@1.18.1:", type=("build", "run"))
	depends_on("r-statnet-common@4.8:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
