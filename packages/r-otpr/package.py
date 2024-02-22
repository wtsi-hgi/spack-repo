# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtpr(RPackage):
	"""An R Wrapper for the 'OpenTripPlanner' REST API

	A wrapper for the 'OpenTripPlanner' <http://www.opentripplanner.org/>
    REST API. Queries are submitted to the relevant 'OpenTripPlanner' API resource, the response
    is parsed and useful R objects are returned.
	"""
	
	cran = "otpr" 

	version("0.5.1", md5="6cd65006749b50a5fdc54b19931c18f6")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rrapply", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
