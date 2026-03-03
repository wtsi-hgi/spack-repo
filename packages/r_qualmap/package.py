# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQualmap(RPackage):
	"""Opinionated Approach for Digitizing Semi-Structured Qualitative
GIS Data

	Provides a set of functions for taking qualitative GIS data, hand drawn on a map, and 
   converting it to a simple features object. These tools are focused on data that are drawn on a map
   that contains some type of polygon features. For each area identified on the map, the id numbers
   of these polygons can be entered as vectors and transformed using qualmap.
	"""
	
	homepage = "https://chris-prener.github.io/qualmap/"
	cran = "qualmap" 

	version("0.2.2", md5="64a5605f5e50f657feebdebf695b40b3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
