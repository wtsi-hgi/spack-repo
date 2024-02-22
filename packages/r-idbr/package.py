# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdbr(RPackage):
	"""R Interface to the US Census Bureau International Data Base API

	Use R to make requests to the US Census Bureau's International Data Base API.
             Results are returned as R data frames.  For more information about the IDB API, visit
             <https://www.census.gov/data/developers/data-sets/international-database.html>.
	"""
	
	cran = "idbr" 

	version("1.0", md5="7fab8f53b829e0f5a5238e69d9385f83")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rnaturalearthdata", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
