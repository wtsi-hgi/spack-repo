# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoogletraffic(RPackage):
	"""Google Traffic

	Create geographically referenced traffic data from the Google Maps JavaScript API <https://developers.google.com/maps/documentation/javascript/examples/layer-traffic>.
	"""
	
	homepage = "https://dime-worldbank.github.io/googletraffic/"
	cran = "googletraffic" 

	version("0.1.5", md5="d75d0855c2a0a62f7411a3fab6f5657c")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-googleway", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-plotwidgets", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-webshot2", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-colornamer", type=("build", "run"))
	depends_on("r-schemr", type=("build", "run"))
