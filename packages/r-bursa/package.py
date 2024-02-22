# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBursa(RPackage):
	"""R Wrapper for Bursa Municipality Open Data Portal

	Call the data wrappers for Bursa Metropolitan Municipality's Open Data Portal <https://acikyesil.bursa.bel.tr/>. This will return all datasets stored in different formats. 
	"""
	
	homepage = "https://github.com/ozancanozdemir/bursa"
	cran = "bursa" 

	version("0.1.0", md5="bf30fcf6ceab1b2eda51af7e335523ea")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
