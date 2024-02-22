# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapboxapi(RPackage):
	"""R Interface to 'Mapbox' Web Services

	Includes support for 'Mapbox' Navigation APIs, including directions, 
  isochrones, and route optimization; the Search API for forward and reverse geocoding; 
  the Maps API for interacting with 'Mapbox' vector tilesets and visualizing 
  'Mapbox' maps in R; and 'Mapbox Tiling Service' and 'tippecanoe' for generating map tiles.
  See <https://docs.mapbox.com/api/> for more information about the 'Mapbox' APIs.
	"""
	
	cran = "mapboxapi" 

	version("0.5.3", md5="23a56a406ec86f51a7835ce32aa93306")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-aws-s3", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-slippymath", type=("build", "run"))
	depends_on("r-protolite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
