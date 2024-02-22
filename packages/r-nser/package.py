# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNser(RPackage):
	"""Bhavcopy and Live Market Data from National Stock Exchange (NSE)
& Bombay Stock Exchange (BSE) India

	Download Current & Historical Bhavcopy. Get Live Market data from NSE India of Equities and Derivatives (F&O) segment. Data source  <https://www.nseindia.com/>. 
	"""
	
	homepage = "https://github.com/nandp1/nser/"
	cran = "nser" 

	version("1.5.1", md5="ad61098083b0767d0c13cfb36092e977")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-googlevis", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
