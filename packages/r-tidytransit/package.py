# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidytransit(RPackage):
	"""Read, Validate, Analyze, and Map GTFS Feeds

	Read General Transit Feed Specification (GTFS) zipfiles into a list of R dataframes. Perform validation of the data structure against the specification. Analyze the headways and frequencies at routes and stops. Create maps and perform spatial analysis on the routes and stops. Please see the GTFS documentation here for more detail: <https://gtfs.org/>.
	"""
	
	homepage = "https://github.com/r-transit/tidytransit"
	cran = "tidytransit" 

	version("1.6.1", md5="2050409bed23ce95851e75b6ac2cffbc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-gtfsio@1.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
