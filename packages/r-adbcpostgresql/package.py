# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdbcpostgresql(RPackage):
	"""'Arrow' Database Connectivity ('ADBC') 'PostgreSQL' Driver

	Provides a developer-facing interface to the 'Arrow' Database
  Connectivity ('ADBC') 'PostgreSQL' driver for the purposes of building high-level
  database interfaces for users. 'ADBC' <https://arrow.apache.org/adbc/> is
  an API standard for database access libraries that uses 'Arrow' for result
  sets and query parameters.
	"""
	
	homepage = "https://github.com/apache/arrow-adbc"
	cran = "adbcpostgresql"

	version("0.10.0", md5="5b5d98bba3d741c41a09b7b4b3051008")

	depends_on("r-adbcdrivermanager", type=("build", "run"))
	depends_on("postgresql+client_only", type=("build", "link", "run"))
