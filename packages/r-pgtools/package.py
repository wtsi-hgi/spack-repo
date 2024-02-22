# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgtools(RPackage):
	"""Functions for Generating PostgreSQL Statements/Scripts

	Create PostgreSQL statements/scripts from R, optionally executing the SQL statements.
    Common SQL operations are included, although not every configurable option is available at this time. 
    SQL output is intended to be compliant with PostgreSQL syntax specifications. PostgreSQL documentation is available here
    <https://www.postgresql.org/docs/current/index.html>.
	"""
	
	homepage = "https://github.com/tconwell/pgTools"
	cran = "pgTools" 

	version("1.0.2", md5="5f09c117d1a8dca9476c0f497e2797fa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-toolbox", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-odbc", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
