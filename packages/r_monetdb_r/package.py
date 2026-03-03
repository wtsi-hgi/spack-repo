# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonetdbR(RPackage):
	"""Connect MonetDB to R

	Allows to pull data from MonetDB into R. 
	"""
	
	homepage = "http://www.monetdb.org"
	cran = "MonetDB.R" 

	version("2.0.0", md5="1e5c8415f8864d51eb32e6d7c2679782")

	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-digest@0.6.4:", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
