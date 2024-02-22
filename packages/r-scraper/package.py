# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScraper(RPackage):
	"""These Functions Fetch and Extract Text Content from Specified
Web Pages

	The 'scrapeR' package utilizes functions that fetch and extract text content from specified web pages. It handles HTTP errors and parses HTML efficiently. The package can handle hundreds of websites at a time using the scrapeR_in_batches() command.
	"""
	
	cran = "scrapeR" 

	version("0.1.8", md5="aff480e10cc6bb0ca6704450318cad0f")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
