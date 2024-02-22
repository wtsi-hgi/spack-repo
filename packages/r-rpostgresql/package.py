# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpostgresql(RPackage):
	"""R Interface to the 'PostgreSQL' Database System.

	Database interface and PostgreSQL driver for R This package provides a
	Database Interface (DBI) compliant driver for R to access PostgreSQL
	database systems. In order to build and install this package from source,
	PostgreSQL itself must be present your system to provide PostgreSQL
	functionality via its libraries and header files. These files are provided
	as postgresql-devel package under some Linux distributions. On Microsoft
	Windows system the attached libpq library source will be used. A wiki and
	issue tracking system for the package are available at Google Code at
	https://code.google.com/p/rpostgresql/."""

	cran = "RPostgreSQL"

	version("0.7-6", md5="81dcb7ee798d531be609996435422b75")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-dbi@0.3:", type=("build", "run"))
	depends_on("postgresql+client_only", type=("build", "link", "run"))
