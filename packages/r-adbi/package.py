# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdbi(RPackage):
	"""'DBI' Compliant Database Access Using 'ADBC'

	In order to make Arrow Database Connectivity ('ADBC' <https://arrow.apache.org/adbc/>) accessible from R, an interface compliant with the 'DBI' package is provided, using driver back-ends that are implemented in the 'adbcdrivermanager' framework. This enables interacting with database systems using the Arrow data format, thereby offering an efficient alternative to 'ODBC' for analytical applications.
	"""
	
	homepage = "https://adbi.r-dbi.org"
	cran = "adbi" 

	version("0.1.1", md5="c5dd96f79307c563564d69e085135d03")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dbi@1.2:", type=("build", "run"))
	depends_on("r-adbcdrivermanager@0.8:", type=("build", "run"))
	depends_on("r-nanoarrow@0.3:", type=("build", "run"))
