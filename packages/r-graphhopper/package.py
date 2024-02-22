# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphhopper(RPackage):
	"""An R Interface to the 'GraphHopper' Directions API

	Provides a quick and easy access to the 'GraphHopper' Directions API.
  'GraphHopper' <https://www.graphhopper.com/> itself is a routing engine based on 'OpenStreetMap' data.
  API responses can be converted to simple feature (sf) objects in a convenient way. 
	"""
	
	homepage = "https://github.com/crazycapivara/graphhopper-r"
	cran = "graphhopper" 

	version("0.1.2", md5="e69b12bc527929ca3c700f4d482bf446")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-googlepolylines", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
