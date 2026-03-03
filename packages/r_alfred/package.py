# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlfred(RPackage):
	"""Downloading Time Series from ALFRED Database for Various
Vintages

	Provides direct access to the ALFRED (<https://alfred.stlouisfed.org>) and FRED (<https://fred.stlouisfed.org>) databases.
    Its functions return tidy data frames for different releases of the specified time series. 
    Note that this product uses the FRED© API but is not endorsed or certified by the Federal Reserve Bank of St. Louis.
	"""
	
	homepage = "https://github.com/onnokleen/alfred/"
	cran = "alfred" 

	version("0.2.1", md5="8bae4c9c7d0bd56e45c9c1bc4cf45f64")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
