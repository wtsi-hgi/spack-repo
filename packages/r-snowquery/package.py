# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnowquery(RPackage):
	"""Query 'Snowflake' Databases with 'SQL'

	A wrapper allowing 'SQL' queries to be run on a 'Snowflake' instance directly from an 'R' script, by using the 'snowflake-connector-python' package in the background.
	"""
	
	homepage = "https://github.com/mermelstein/snowquery"
	cran = "snowquery" 

	version("1.0.0", md5="8eea0fc2ecd14d7f629d0c1577acb867")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rpostgres", type=("build", "run"))
