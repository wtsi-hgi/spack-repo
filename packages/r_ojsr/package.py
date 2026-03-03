# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROjsr(RPackage):
	"""Crawler and Data Scraper for Open Journal System ('OJS')

	Crawler for 'OJS' pages and scraper for meta-data from articles. 
    You can crawl 'OJS' archives, issues, articles, galleys, and search results. 
    You can scrape articles metadata from their head tag in html, 
    or from Open Archives Initiative ('OAI') records.
    Most of these functions rely on 'OJS' routing conventions 
    (<https://docs.pkp.sfu.ca/dev/documentation/en/architecture-routes>).
	"""
	
	cran = "ojsr" 

	version("0.1.2", md5="03a01cbfd97f5be5dee1b6750e17bb6d")

	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
