# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYfr(RPackage):
	"""Downloads and Organizes Financial Data from Yahoo Finance

	Facilitates download of financial data from Yahoo Finance <https://finance.yahoo.com/>, 
 a vast repository of stock price data across multiple financial exchanges. The package offers a local caching system
 and support for parallel computation.
	"""
	
	homepage = "https://github.com/ropensci/yfR"
	cran = "yfR" 

	version("1.1.0", md5="3de7ce83a7169c484e86aa2f581a1174")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-quantmod@0.4.20:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-humanize", type=("build", "run"))
	depends_on("r-pingr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
