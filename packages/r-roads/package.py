# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoads(RPackage):
	"""Road Network Projection

	Project road network development based on an existing road 
    network, target locations to be connected by roads and a cost surface. Road 
    projection methods include minimum spanning tree with least cost path 
    (Kruskal's algorithm (1956) <doi:10.2307/2033241>), least cost path 
    (Dijkstra's algorithm (1959) <doi:10.1007/BF01386390>) or snapping. 
    These road network projection methods are ideal for use with land cover
    change projection models.
	"""
	
	homepage = "https://github.com/LandSciTech/roads"
	cran = "roads" 

	version("1.1.1", md5="2960f49fa64c363ec480fc2e8e6dc986")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
