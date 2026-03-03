# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfluxdbr(RPackage):
	"""R Interface to InfluxDB

	An R interface to the InfluxDB time series database <https://www.influxdata.com>. This package allows you to fetch and write time series data from/to an InfluxDB server. Additionally, handy wrappers for the Influx Query Language (IQL) to manage and explore a remote database are provided. 
	"""
	
	homepage = "https://github.com/dleutnant/influxdbr"
	cran = "influxdbr" 

	version("0.14.2", md5="7311e5f3b5081afb54baa11de2ad6cb1")

	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@0.2.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
