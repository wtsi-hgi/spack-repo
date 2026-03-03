# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebird(RPackage):
	"""R Client for the eBird Database of Bird Observations

	A programmatic client for the eBird database 
    (<https://ebird.org/home>), including functions for searching for bird 
    observations by geographic location (latitude, longitude), eBird 
    hotspots, location identifiers, by notable sightings, by region, and by 
    taxonomic name.
	"""
	
	homepage = "https://docs.ropensci.org/rebird/"
	cran = "rebird" 

	version("1.3.0", md5="85a6d184e24cf6ee82acdeffdf1b1a58")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
