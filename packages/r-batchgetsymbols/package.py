# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchgetsymbols(RPackage):
	"""Downloads and Organizes Financial Data for Multiple Tickers

	Makes it easy to download financial data from Yahoo Finance <https://finance.yahoo.com/>.
	"""
	
	cran = "BatchGetSymbols" 

	version("2.6.4", md5="21c97c1719a3332f352f0e02f1d8ebbc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
