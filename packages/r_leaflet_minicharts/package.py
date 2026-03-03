# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafletMinicharts(RPackage):
	"""Mini Charts for Interactive Maps

	Add and modify small charts on an interactive map created with 
    package 'leaflet'. These charts can be used to represent at same time multiple 
    variables on a single map.
	"""
	
	cran = "leaflet.minicharts" 

	version("0.6.2", md5="388fdcf1f62774545815457688d3b395")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-leaflet@1.1:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
