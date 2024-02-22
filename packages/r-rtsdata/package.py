# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtsdata(RPackage):
	"""R Time Series Intelligent Data Storage

	A tool that allows to download and save historical time series data 
	for future use offline. The intelligent updating functionality will only download 
	the new available information; thus, saving you time and Internet bandwidth. 
	It will only re-download the full data-set if any inconsistencies are detected. 
	This package supports following data provides: 'Yahoo' (finance.yahoo.com), 
	'FRED' (fred.stlouisfed.org), 'Quandl' (data.nasdaq.com), 
	'AlphaVantage' (www.alphavantage.co), 'Tiingo' (www.tiingo.com).
	"""
	
	homepage = "https://bitbucket.org/rtsvizteam/rtsdata"
	cran = "rtsdata" 

	version("0.1.4", md5="3eb3dc0ed7d03c10cdf32c0a50818e11")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-quandl", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mongolite", type=("build", "run"))
	depends_on("r-brotli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
