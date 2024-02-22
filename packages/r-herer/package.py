# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHerer(RPackage):
	"""'sf'-Based Interface to the 'HERE' REST APIs

	Interface to the 'HERE' REST APIs <https://developer.here.com/develop/rest-apis>:
  (1) geocode and autosuggest addresses or reverse geocode POIs using the 'Geocoder' API;
  (2) route directions, travel distance or time matrices and isolines using the 'Routing', 'Matrix Routing' and 'Isoline Routing' APIs;
  (3) request real-time traffic flow and incident information from the 'Traffic' API;
  (4) find request public transport connections and nearby stations from the 'Public Transit' API;
  (5) request intermodal routes using the 'Intermodal Routing' API;
  (6) get weather forecasts, reports on current weather conditions, astronomical
  information and alerts at a specific location from the 'Destination Weather' API.
  Locations, routes and isolines are returned as 'sf' objects.
	"""
	
	homepage = "https://munterfi.github.io/hereR/"
	cran = "hereR" 

	version("1.0.0", md5="e4cbd2d86a6ee6ba23cf0e2c329541d5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-crul@1.1:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-flexpolyline@0.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-sf@0.9.0:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
