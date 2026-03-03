# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhitewater(RPackage):
	"""Parallel Processing Options for Package 'dataRetrieval'

	Provides methods for retrieving United States Geological Survey (USGS) water data using sequential and parallel processing (Bengtsson, 2022 <doi:10.32614/RJ-2021-048>). In addition to parallel methods, data wrangling and additional statistical attributes are provided. 
	"""
	
	homepage = "https://github.com/joshualerickson/whitewater/"
	cran = "whitewater" 

	version("0.1.3", md5="92920d82f6ac25f96f2665c6dcc3fa67")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dataretrieval", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
