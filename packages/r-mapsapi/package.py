# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapsapi(RPackage):
	"""'sf'-Compatible Interface to 'Google Maps' APIs

	Interface to the 'Google Maps' APIs: (1) routing directions based on the 'Directions' API, returned as 'sf' objects, either as single feature per alternative route, or a single feature per segment per alternative route; (2) travel distance or time matrices based on the 'Distance Matrix' API; (3) geocoded locations based on the 'Geocode' API, returned as 'sf' objects, either points or bounds; (4) map images using the 'Maps Static' API, returned as 'stars' objects.
	"""
	
	homepage = "https://michaeldorman.github.io/mapsapi/"
	cran = "mapsapi" 

	version("0.5.4", md5="8e5f1c0b8ede59314e83ac29b2f3e363")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-rgooglemaps", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
