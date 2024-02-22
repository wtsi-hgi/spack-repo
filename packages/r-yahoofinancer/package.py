# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYahoofinancer(RPackage):
	"""Fetch Data from Yahoo Finance API

	Obtain historical and near real time data related to stocks, index 
    and currencies from the Yahoo Finance API. This package is community maintained 
    and is not officially supported by 'Yahoo'. The accuracy of data is only as 
    correct as provided on <https://finance.yahoo.com/>.
	"""
	
	homepage = "https://yahoofinancer.rsquaredacademy.com/"
	cran = "yahoofinancer" 

	version("0.3.0", md5="c58b3df9c178bd5f3865589b0ce4bd22")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
