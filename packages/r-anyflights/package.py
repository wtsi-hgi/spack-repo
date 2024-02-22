# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnyflights(RPackage):
	"""Query 'nycflights13'-Like Air Travel Data for Given Years and
Airports

	Supplies a set of functions to query air travel data for user-
    specified years and airports. Datasets include on-time flights, airlines,
    airports, planes, and weather.
	"""
	
	homepage = "https://github.com/simonpcouch/anyflights"
	cran = "anyflights" 

	version("0.3.4", md5="5966512890e70040d71c7ca496959dcd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
