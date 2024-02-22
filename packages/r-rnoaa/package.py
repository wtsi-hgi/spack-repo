# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnoaa(RPackage):
	"""'NOAA' Weather Data from R.

	Client for many 'NOAA' data sources including the 'NCDC' climate 'API' at
	<https://www.ncdc.noaa.gov/cdo-web/webservices/v2>, with functions for each
	of the 'API' 'endpoints': data, data categories, data sets, data types,
	locations, location categories, and stations. In addition, we have an
	interface for 'NOAA' sea ice data, the 'NOAA' severe weather inventory,
	'NOAA' Historical Observing 'Metadata' Repository ('HOMR') data, 'NOAA'
	storm data via 'IBTrACS', tornado data via the 'NOAA' storm prediction
	center, and more."""

	cran = "rnoaa"

	version("1.4.0", md5="5fb8dc93d638d98710452c90e0adb31c")

	depends_on("r-crul@0.7:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-isdparser@0.2:", type=("build", "run"))
	depends_on("r-geonames", type=("build", "run"))
	depends_on("r-hoardr@0.5.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
