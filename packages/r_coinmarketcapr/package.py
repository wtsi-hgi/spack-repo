# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoinmarketcapr(RPackage):
	"""Get 'Cryptocurrencies' Market Cap Prices from Coin Market Cap

	Extract and monitor price and market cap of 'Cryptocurrencies' from 'Coin Market Cap' <https://coinmarketcap.com/api/>. 
	"""
	
	homepage = "https://github.com/amrrs/coinmarketcapr"
	cran = "coinmarketcapr" 

	version("0.4", md5="2d6d1bba62c3a82ef592c31d941e43a9")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
