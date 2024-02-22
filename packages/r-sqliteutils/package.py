# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqliteutils(RPackage):
	"""Utility Functions for 'SQLite'

	A tool for working with 'SQLite' databases. 'SQLite' has some idiosyncrasies and limitations that impose some hurdles to the R developer who is using this database as a repository. For instance, 'SQLite' doesn't have a date type and 'sqliteutils' has some functions to deal with that.
	"""
	
	cran = "sqliteutils" 

	version("0.1.0", md5="f542f8ab49143ac1c7b83763857420d7")

	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
