# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNzffdr(RPackage):
	"""Import, Clean and Update Data from the New Zealand Freshwater
Fish Database

	Access the New Zealand Freshwater Fish Database from R and a few functions to clean the data once in R.
	"""
	
	homepage = "https://flee598.github.io/nzffdr/"
	cran = "nzffdr" 

	version("2.1.0", md5="392908877a1c049cb4770167d4447186")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
