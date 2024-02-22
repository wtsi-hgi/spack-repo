# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCryptowatchr(RPackage):
	"""An API Wrapper for 'Cryptowatch'

	An API wrapper for 'Cryptowatch' to get prices and other information (e.g., volume, trades, order books, bid and ask prices, live quotes, and more) about cryptocurrencies and crypto exchanges. See <https://docs.cryptowat.ch/rest-api> for a detailed documentation.
	"""
	
	homepage = "https://github.com/lorenzbr/cryptowatchR"
	cran = "cryptowatchR" 

	version("0.2.0", md5="98c0f39aa1c4293b1557d2f380ab582d")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
