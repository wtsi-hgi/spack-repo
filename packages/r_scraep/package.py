# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScraep(RPackage):
	"""Scrape the Web with Extra Power

	Tools for scraping information from webpages and other XML contents, using XPath or CSS selectors.
	"""
	
	cran = "scraEP" 

	version("1.2", md5="c1348a162e02b8998ea5180291b6922e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
