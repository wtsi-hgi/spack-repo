# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdbc(RPackage):
	"""Connect to ODBC Compatible Databases (using the DBI Interface)

	A DBI-compatible interface to ODBC databases.
	"""
	
	homepage = "https://odbc.r-dbi.org"
	cran = "odbc" 

	version("1.4.2", md5="73f3a4c6ce2aff62a070d7220e86a6dd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-blob@1.2:", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("unixodbc", type=("build", "link", "run"))
