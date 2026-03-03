# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRalger(RPackage):
	"""Easy Web Scraping

	The goal of 'ralger' is to facilitate web scraping in R. 
	"""
	
	homepage = "https://github.com/feddelegrand7/ralger"
	cran = "ralger" 

	version("2.2.4", md5="b2364cf526a3824d4ade5b065e72e3a0")

	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-robotstxt", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
