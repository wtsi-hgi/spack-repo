# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetquandldata(RPackage):
	"""Fast and Cached Import of Data from 'Quandl' Using the 'json
API'

	Imports time series data from the 'Quandl' database <https://data.nasdaq.com/>. The package uses the  'json api' at <https://data.nasdaq.com/search>, local caching ('memoise' package) and the tidy format by default. 
   Also allows queries of databases, allowing the user to see which time series are available for each database id. In short, it is an alternative to package 'Quandl', with faster data importation in the tidy/long format.
	"""
	
	homepage = "https://github.com/msperlin/GetQuandlData/"
	cran = "GetQuandlData" 

	version("1.0.0", md5="1e383a6d5472e0089f2ad10a59157598")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
