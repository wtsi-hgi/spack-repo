# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialgraph(RPackage):
	"""The SpatialGraph Class and Utilities

	Provision of the S4 SpatialGraph class built on top of objects provided by 'igraph' and 'sp' packages, and associated utilities. See the documentation of the SpatialGraph-class within this package for further description. An example of how from a few points one can arrive to a SpatialGraph is provided in the function sl2sg().  
	"""
	
	homepage = "https://github.com/garciapintado/SpatialGraph"
	cran = "SpatialGraph" 

	version("1.0-4", md5="72c9d0e17d9bc326c5fe32e7603c53e6")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
