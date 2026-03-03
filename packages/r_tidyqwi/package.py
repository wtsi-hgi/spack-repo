# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyqwi(RPackage):
	"""A Convenient API for Accessing United States Census Bureau's
Quarterly Workforce Indicator

	The purpose of this package is to access the 
    United States Census Bureau's Quarterly Workforce Indicator data. Additionally, 
    the data will be retrieved in a tidy format for further manipulation with full variable
    descriptions added if desired. Information about the United States Census Bureau's 
    Quarterly Workforce Indicator is available at 
    <https://www.census.gov/data/developers/data-sets/qwi.html>.
	"""
	
	cran = "tidyqwi" 

	version("0.1.2", md5="e793603b48f43983ce45419a6c8a363c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-future@1.6.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
