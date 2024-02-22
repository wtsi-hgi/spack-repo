# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtfsrouter(RPackage):
	"""Routing with 'GTFS' (General Transit Feed Specification) Data

	Use 'GTFS' (General Transit Feed Specification) data for routing
    from nominated start and end stations, for extracting 'isochrones', and
    travel times from any nominated start station to all other stations.
	"""
	
	homepage = "https://github.com/UrbanAnalyst/gtfsrouter"
	cran = "gtfsrouter" 

	version("0.1.2", md5="7f663f592994fd512181a81585d06b6e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
