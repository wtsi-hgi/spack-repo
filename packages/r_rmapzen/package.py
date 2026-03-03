# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmapzen(RPackage):
	"""Client for 'Mapzen' and Related Map APIs

	Provides an interface to 'Mapzen'-based APIs (including 
    geocode.earth, Nextzen, and NYC GeoSearch) for geographic search 
    and geocoding, isochrone calculation, and vector data to draw map tiles. 
    See <https://www.mapzen.com/documentation/> for more information. The original 
    Mapzen has gone out of business, but 'rmapzen' can be set up to work with 
    any provider who implements the Mapzen API. 
	"""
	
	homepage = "https://tarakc02.github.io/rmapzen/"
	cran = "rmapzen" 

	version("0.5.1", md5="a11a4216a6120c53c333091f79741531")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-isocodes", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-geojsonio", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
