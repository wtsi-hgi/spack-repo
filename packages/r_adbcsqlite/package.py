# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdbcsqlite(RPackage):
	"""'Arrow' Database Connectivity ('ADBC') 'SQLite' Driver

	Provides a developer-facing interface to the 'Arrow' Database
  Connectivity ('ADBC') 'SQLite' driver for the purposes of building high-level
  database interfaces for users. 'ADBC' <https://arrow.apache.org/adbc/> is
  an API standard for database access libraries that uses 'Arrow' for result
  sets and query parameters.
	"""
	
	homepage = "https://github.com/apache/arrow-adbc"
	cran = "adbcsqlite"

	version("0.9.0", md5="f451684e4e0c269bcdd27b70038f82d1")
	version("0.10.0", md5="fb28cadb38c04050e8a95a7113e3cf30")

	depends_on("r-adbcdrivermanager", type=("build", "run"))
	depends_on("sqlite@3:", type=("build", "link", "run"))
