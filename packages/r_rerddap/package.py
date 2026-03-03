# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRerddap(RPackage):
	"""General Purpose Client for 'ERDDAP' Servers

	General purpose R client for 'ERDDAP' servers. Includes
    functions to search for 'datasets', get summary information on
    'datasets', and fetch 'datasets', in either 'csv' or 'netCDF' format.
    'ERDDAP' information: 
    <https://upwell.pfeg.noaa.gov/erddap/information.html>.
	"""
	
	homepage = "https://docs.ropensci.org/rerddap/"
	cran = "rerddap" 

	version("1.1.0", md5="9f652a877d3d2763c7e21f32dc4b522a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-crul@0.7.4:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-hoardr@0.5.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ncdf4@1.16:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
