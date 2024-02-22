# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfluxdbclient(RPackage):
	"""'InfluxDB' 2.x Client

	
  'InfluxDB' 2.x time-series database client. Supports both 'InfluxDB' OSS (<https://portal.influxdata.com/downloads/>) and Cloud (<https://cloud2.influxdata.com/>) version.
	"""
	
	homepage = "https://github.com/influxdata/influxdb-client-r"
	cran = "influxdbclient" 

	version("0.1.2", md5="398f45864fb268441eea04a1033978be")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-nanotime@0.3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
