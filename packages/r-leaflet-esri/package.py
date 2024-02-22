# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafletEsri(RPackage):
	"""'ESRI' Bindings for the 'leaflet' Package

	An add-on package to the 'leaflet' package, which provides bindings for 'ESRI' services. This package allows a user to add 'ESRI' provided services such as 'MapService', 'ImageMapService', 'TiledMapService' etc. to a 'leaflet' map.
	"""
	
	homepage = "https://github.com/bhaskarvk/leaflet.esri"
	cran = "leaflet.esri" 

	version("1.0.0", md5="6f78c9e4943634f2cf51de67be7a4607")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-leaflet@2:", type=("build", "run"))
	depends_on("r-leaflet-extras@1:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
