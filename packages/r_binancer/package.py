# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinancer(RPackage):
	"""API Client to 'Binance'

	R client to the 'Binance' Public Rest API for data collection on cryptocurrencies, portfolio management and trading: <https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md>.
	"""
	
	homepage = "https://daroczig.github.io/binancer/"
	cran = "binancer" 

	version("1.2.0", md5="f0658d581d1da26fd8e59c7e17459d76")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
