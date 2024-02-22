# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMazamaspatialutils(RPackage):
	"""Spatial Data Download and Utility Functions

	A suite of conversion functions to create internally standardized
    spatial polygons data frames. Utility functions use these data sets to
    return values such as country, state, time zone, watershed, etc. associated
    with a set of longitude/latitude pairs. (They also make cool maps.)
	"""
	
	homepage = "https://github.com/MazamaScience/MazamaSpatialUtils"
	cran = "MazamaSpatialUtils" 

	version("0.8.6", md5="35b6ef74d9cdc13ff5a3ab0342dba214")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mazamacoreutils@0.4.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmapshaper", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
