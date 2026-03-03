# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedquant(RPackage):
	"""Public Economic Data and Quantitative Analysis

	
    Provides an interface to access public economic and financial data for 
    economic research and quantitative analysis. The data sources including 
    NBS, FRED, Sina, Eastmoney and etc. It also provides quantitative 
    functions for trading strategies based on the 'data.table', 'TTR', 
    'PerformanceAnalytics' and etc packages.
	"""
	
	homepage = "https://github.com/ShichenXie/pedquant"
	cran = "pedquant" 

	version("0.2.4", md5="2a8e3e969f314c22833d122a2cfb7938")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-echarts4r", type=("build", "run"))
	depends_on("r-xefun@0.1.3:", type=("build", "run"))
