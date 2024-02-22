# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeseriesdb(RPackage):
	"""A Time Series Database for Official Statistics with R and
PostgreSQL

	Archive and manage times series data from official statistics. The 'timeseriesdb' package was designed to manage a large catalog of time series from official statistics which are typically published on a monthly, quarterly or yearly basis. Thus timeseriesdb is optimized to handle updates caused by data revision as well as elaborate, multi-lingual meta information. 
	"""
	
	homepage = "https://github.com/mbannert/timeseriesdb"
	cran = "timeseriesdb" 

	version("1.0.0-1.1.2", md5="12f4d39283ff46298c47322d5c28d180")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rpostgres@1.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.1:", type=("build", "run"))
	depends_on("r-data-table@1.9.4:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
