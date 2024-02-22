# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtvapi(RPackage):
	"""Access the 'Public Transport Victoria' Timetable API

	Access the 'Public Transport Victoria' Timetable API 
    <https://www.ptv.vic.gov.au/footer/data-and-reporting/datasets/ptv-timetable-api/>,
    with results returned as familiar R data structures. Retrieve information on
    stops, routes, disruptions, departures, and more.
	"""
	
	homepage = "https://github.com/mdneuzerling/ptvapi"
	cran = "ptvapi" 

	version("2.0.5", md5="dc82ff0ab9c67318e969fde84cc19812")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
