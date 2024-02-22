# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRusquant(RPackage):
	"""Quantitative Trading Framework

	Collection of functions to retrieve financial data from various sources, including brokerage and exchange platforms, financial websites, and data providers. Includes functions to retrieve account information, portfolio information, and place/cancel orders from different brokers. Additionally, allows users to download historical data such as earnings, dividends, stock splits.
	"""
	
	homepage = "https://rusquant.ru"
	cran = "rusquant" 

	version("1.0.5", md5="58eaa1b9071687ec63dd02283adc738e")

	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jose", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
