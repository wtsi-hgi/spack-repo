# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClickhousehttp(RPackage):
	"""A Simple HTTP Database Interface to 'ClickHouse'

	'ClickHouse' (<https://clickhouse.com/>)
   is an open-source, high performance columnar
   OLAP (online analytical processing of queries) database management system
   for real-time analytics using SQL. This 'DBI' backend
   relies on the 'ClickHouse' HTTP interface and support HTTPS protocol.
	"""
	
	homepage = "https://github.com/patzaw/ClickHouseHTTP"
	cran = "ClickHouseHTTP" 

	version("0.3.2", md5="c83ad5bc768c348cd4159ba9000cb98e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dbi@0.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
