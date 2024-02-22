# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsql(RPackage):
	"""Database Agnostic Package to Generate and Process 'SQL' Queries
in R

	Allows the user to generate and execute select, insert, update and delete 'SQL' queries the underlying database without having to explicitly write 'SQL' code. 
	"""
	
	homepage = "https://github.com/rOpenStats/RSQL"
	cran = "RSQL" 

	version("0.2.2", md5="641d4d3ea4eaf40702de7f4d02f19bb4")

	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
