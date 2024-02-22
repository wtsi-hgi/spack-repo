# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeodrawr(RPackage):
	"""Making Geospatial Objects

	Draw geospatial objects by clicks on the map.
    This packages can help data analyst who want to check
    their own geospatial hypothesis but has no ready-made geospatial objects.
	"""
	
	homepage = "https://github.com/Curycu/geodrawr"
	cran = "geodrawr" 

	version("2.0.0", md5="8676d7b1bdcb5b92fb324b49ebbcf72d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sf@0.9.0:", type=("build", "run"))
	depends_on("r-leaflet@2:", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7:", type=("build", "run"))
