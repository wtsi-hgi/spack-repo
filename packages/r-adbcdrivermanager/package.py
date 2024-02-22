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

	version("0.9.0.1", md5="fdafe6ce85e727e21c175e87dd8d80e1")

	depends_on("r-nanoarrow@0.3:", type=("build", "run"))
