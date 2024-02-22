# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStampr(RPackage):
	"""Spatial Temporal Analysis of Moving Polygons

	Perform spatial temporal analysis of moving polygons; a
    longstanding analysis problem in Geographic Information Systems. Facilitates
    directional analysis, distance analysis, and some other simple functionality for
    examining spatial-temporal patterns of moving polygons.
	"""
	
	homepage = "https://github.com/jedalong/stampr"
	cran = "stampr" 

	version("0.3.1", md5="0dff66442629630d6d28350bec91f544")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
