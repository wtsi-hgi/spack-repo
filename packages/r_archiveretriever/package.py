# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchiveretriever(RPackage):
	"""Retrieve Archived Web Pages from the 'Internet Archive'

	Scraping content from archived web pages stored in
    the 'Internet Archive' (<https://archive.org>) using a systematic
    workflow.  Get an overview of the mementos available from the
    respective homepage, retrieve the Urls and links of the page and
    finally scrape the content. The final output is stored in tibbles,
    which can be then easily used for further analysis.
	"""
	
	homepage = "https://github.com/liserman/archiveRetriever/"
	cran = "archiveRetriever" 

	version("0.3.1", md5="d8bd8869bad771c00c1646dfd6fe18f5")

	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
