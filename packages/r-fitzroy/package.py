# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitzroy(RPackage):
	"""Easily Scrape and Process AFL Data

	An easy package for scraping and processing Australia Rules Football (AFL)
    data. 'fitzRoy' provides a range of functions for accessing publicly available data 
    from 'AFL Tables' <https://afltables.com/afl/afl_index.html>, 'Footy Wire' <https://www.footywire.com> and
    'The Squiggle' <https://squiggle.com.au>. Further functions allow for easy processing, 
    cleaning and transformation of this data into formats that can be used for analysis. 
	"""
	
	homepage = "https://jimmyday12.github.io/fitzRoy/"
	cran = "fitzRoy" 

	version("1.3.0", md5="189992d72ddf2f5398afdea519bb393b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
