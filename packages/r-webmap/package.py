# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebmap(RPackage):
	"""Create Interactive Web Maps Using 'The National Map' Services

	Creates interactive web maps using the 'JavaScript' 'Leaflet'
    library with base layers of 'The National Map' ('TNM'). 'TNM' services
    provide access to base geospatial information that describes the landscape
    of the United States and its territories. This package is dependent on, and
    intended to be used with, the 'leaflet' package.
	"""
	
	homepage = "https://rconnect.usgs.gov/INLPO/webmap-main/"
	cran = "webmap" 

	version("1.0.7", md5="2d7bd9c678e880bd2e5abd74874ae847")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
