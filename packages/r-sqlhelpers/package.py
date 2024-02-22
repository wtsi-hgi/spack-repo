# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqlhelpers(RPackage):
	"""Collection of 'SQL' Utilities for 'T-SQL' and 'Postgresql'

	Includes functions for interacting with common meta data fields, 
  writing insert statements, calling functions, and more for 'T-SQL' and 'Postgresql'.
	"""
	
	cran = "sqlHelpers" 

	version("0.1.2", md5="da8a80341e5ae4bd14fc7a5c7339d93d")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-toolbox", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-odbc", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
