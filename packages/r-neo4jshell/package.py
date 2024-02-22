# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeo4jshell(RPackage):
	"""Querying and Managing 'Neo4J' Databases in 'R'

	Sends queries to a specified 'Neo4J' graph database, capturing results in a dataframe where appropriate.  
    Other useful functions for the importing and management of data on the 'Neo4J' server and basic local server admin.  
	"""
	
	cran = "neo4jshell" 

	version("0.1.2", md5="66fae912131a5a528f54faa14036241d")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ssh", type=("build", "run"))
	depends_on("r-sys", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("neo4j", type=("build", "link", "run"))
