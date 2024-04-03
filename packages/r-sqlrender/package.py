# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqlrender(RPackage):
	"""Rendering Parameterized SQL and Translation to Dialects

	A rendering tool for parameterized SQL that also translates into
  different SQL dialects.  These dialects include 'Microsoft SQL Server', 'Oracle', 
  'PostgreSql', 'Amazon RedShift', 'Apache Impala', 'IBM Netezza', 'Google BigQuery', 'Microsoft PDW', 'Snowflake', 
  'Azure Synapse Analytics Dedicated', 'Apache Spark', and 'SQLite'.
	"""
	
	homepage = "https://ohdsi.github.io/SqlRender/"
	cran = "SqlRender" 

	version("1.17.0", md5="ec10766001ac7466e77c5c9e2eb4d48f")

	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
