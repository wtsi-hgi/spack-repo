# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatabaseconnector(RPackage):
	"""Connecting to Various Database Platforms

	An R 'DataBase Interface' ('DBI') compatible interface to various database platforms ('PostgreSQL', 'Oracle', 'Microsoft SQL Server', 
    'Amazon Redshift', 'Microsoft Parallel Database Warehouse', 'IBM Netezza', 'Apache Impala', 'Google BigQuery', 'Snowflake', 'Spark', and 'SQLite'). Also includes support for
    fetching data as 'Andromeda' objects. Uses either 'Java Database Connectivity' ('JDBC') or other 'DBI' drivers to connect to databases.
	"""
	
	homepage = "https://ohdsi.github.io/DatabaseConnector/"
	cran = "DatabaseConnector" 

	version("6.3.2", md5="c2f2b2469a21bff3b3f926b07961f081")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-sqlrender@1.16:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dbplyr@2.2:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
