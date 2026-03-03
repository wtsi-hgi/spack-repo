# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocker(RPackage):
	"""Database Interface Class

	'R6' class interface for handling relational database connections using 'DBI' package as backend.
  The class allows handling of connections to e.g. PostgreSQL, MariaDB and SQLite.
  The purpose is having an intuitive object allowing straightforward handling of SQL databases.
	"""
	
	homepage = "https://github.com/nikolaus77/rocker"
	cran = "rocker" 

	version("0.3.1", md5="da56bbfb2c178e82920fe43af2a057ce")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-sodium", type=("build", "run"))
