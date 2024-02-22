# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrypto2(RPackage):
	"""Download Crypto Currency Data from 'CoinMarketCap' without 'API'

	Retrieves crypto currency information and historical prices as well as information on the exchanges they are listed on. Historical data contains daily open, high, low and close values for all crypto currencies. All data is scraped from <https://coinmarketcap.com> via their 'web-api'.
	"""
	
	homepage = "https://github.com/sstoeckl/crypto2"
	cran = "crypto2" 

	version("1.4.6", md5="19c376666871f1002da15a8417605ae3", url="https://cran.r-project.org/src/contrib/crypto2_1.4.6.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
