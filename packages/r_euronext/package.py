# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REuronext(RPackage):
	"""Retrieve Historical Data of Companies Listed on the 'Euronext'
Stock Exchange

	Provides seamless access to historical data of companies listed on the 'Euronext' Stock Exchange (<https://live.euronext.com/en>), enabling users to retrieve real-time information directly within the R environment. With functions tailored for data retrieval and manipulation, users can effortlessly access a wide range of financial data, including stock prices, trading volumes, and more. Leveraging the power of R, this package facilitates efficient analysis and visualization of stock market trends, aiding investors, analysts, and researchers in making informed decisions. By combining ease of use with comprehensive data access, 'Euronext' empowers R users to delve deep into the dynamics of European financial markets, offering valuable insights for various financial applications.
	"""
	
	homepage = "https://rpubs.com/Fredysessie/euronext"
	cran = "Euronext" 

	version("2.0.2", md5="6c4e003a2fd66d031fdb3164caa875ef")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-highcharter", type=("build", "run"))
