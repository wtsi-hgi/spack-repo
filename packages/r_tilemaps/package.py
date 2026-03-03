# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTilemaps(RPackage):
	"""Generate Tile Maps

	Implements an algorithm for generating maps, known as tile maps,
    in which each region is represented by a single tile of the same shape and
    size. The algorithm was first proposed in "Generating Tile Maps" by Graham
    McNeill and Scott Hale (2017) <doi:10.1111/cgf.13200>. Functions allow
    users to generate, plot, and compare square or hexagon tile maps.
	"""
	
	homepage = "https://github.com/kaerosen/tilemaps"
	cran = "tilemaps" 

	version("0.2.0", md5="b5c7ccb77241d17d4bb18f3378fb856e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-smoothr", type=("build", "run"))
