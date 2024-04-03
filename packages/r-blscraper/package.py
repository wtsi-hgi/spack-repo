# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlscraper(RPackage):
	"""An API Wrapper for the United States Bureau of Labor Statistics

	Scrapes various data from <https://www.bls.gov/>. The Bureau of Labor Statistics is the statistical branch of the United States Department of Labor. The package has additional functions to help parse, analyze and visualize the data.
	"""
	
	homepage = "https://github.com/keberwein/blscrapeR"
	cran = "blscrapeR" 

	version("4.0.1", md5="8c5e41e08d1851a151852d4005b93c20")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
