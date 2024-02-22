# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrappy(RPackage):
	"""A Simple Web Scraper

	A group of functions to scrape data from different websites, for 
    academic purposes.
	"""
	
	homepage = "https://github.com/villegar/scrappy/"
	cran = "scrappy" 

	version("0.0.1", md5="917009b50e772a74c340909996a7915d")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
