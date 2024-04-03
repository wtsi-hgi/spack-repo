# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdbcdrivermanager(RPackage):
	"""'Arrow' Database Connectivity ('ADBC') Driver Manager

	Provides a developer-facing interface to 'Arrow' Database
  Connectivity ('ADBC') for the purposes of driver development, driver
  testing, and building high-level database interfaces for users. 'ADBC'
  <https://arrow.apache.org/adbc/> is an API standard for database access
  libraries that uses 'Arrow' for result sets and query parameters.
	"""
	
	homepage = "https://github.com/apache/arrow-adbc"
	cran = "adbcdrivermanager" 

	version("0.10.0", md5="99cb5cdc57201b905c08d8c30590df70")
	version("0.11.0", md5="dd000875d9a46549f07a4cf090ba5b37")

	depends_on("r-nanoarrow@0.3:", type=("build", "run"))
