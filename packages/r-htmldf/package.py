# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmldf(RPackage):
	"""Simple Scraping and Tidy Webpage Summaries

	Simple tools for scraping webpages, extracting common html tags and parsing contents to a tidy, tabular format.  Tools help with extraction of page titles, links, images, rss feeds, social media handles and page metadata.
	"""
	
	homepage = "https://github.com/alastairrushworth/htmldf/"
	cran = "htmldf" 

	version("0.6.0", md5="366a98a81cb6defdfaf87844197bd0c0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cld3", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
