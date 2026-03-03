# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtlasmaker(RPackage):
	"""Make Multiple 'leaflet' Maps in 'Shiny'

	Simplify creating multiple, related 'leaflet' maps across tabs for a 'shiny' application. Users build lists of any polygons, points, and polylines needed for the project, use the map_server() function to assign built lists and other chosen aesthetics into each tab, and the package leverages modules to generate all map tabs.
	"""
	
	homepage = "https://github.com/rachel-greenlee/AtlasMaker"
	cran = "AtlasMaker" 

	version("0.1.0", md5="3f558c79682736a1f7cbbd4685d0dfd3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
