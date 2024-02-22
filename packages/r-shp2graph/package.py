# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShp2graph(RPackage):
	"""Convert a 'SpatialLinesDataFrame' -Class Object to an
'igraph'-Class Object

	Functions for converting and processing network data from a
        'SpatialLinesDataFrame' -Class object to an 'igraph'-Class object.
	"""
	
	cran = "shp2graph" 

	version("1-0", md5="7a6b7aad42af9902e6bdd6043f184a23")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
