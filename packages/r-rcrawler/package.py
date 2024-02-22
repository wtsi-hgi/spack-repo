# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcrawler(RPackage):
	"""Web Crawler and Scraper

	Performs parallel web crawling and web scraping. It is designed to crawl, parse and store web pages to produce data that can be directly used for analysis application. For details see Khalil and Fakir (2017) <DOI:10.1016/j.softx.2017.04.004>.
	"""
	
	homepage = "https://github.com/salimk/Rcrawler/"
	cran = "Rcrawler" 

	version("0.1.9-1", md5="c1dcb9c1ee9c04a8beed16d7104db5d4")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-selectr", type=("build", "run"))
	depends_on("r-webdriver", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
