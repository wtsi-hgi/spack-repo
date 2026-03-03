# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRosm(RPackage):
	"""Plot Raster Map Tiles from Open Street Map and Other Sources

	Download and plot Open Street Map <https://www.openstreetmap.org/>,
    Bing Maps <https://www.bing.com/maps> and other tiled map sources. Use to create 
    basemaps quickly and add hillshade to vector-based maps.
	"""
	
	homepage = "https://github.com/paleolimbot/rosm"
	cran = "rosm" 

	version("0.3.0", md5="1081f968d9ca249ad6d6b478f74caf4f")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-wk", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
