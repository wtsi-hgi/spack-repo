# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKiwisr(RPackage):
	"""A Wrapper for Querying KISTERS 'WISKI' Databases via the 'KiWIS'
API

	A wrapper for querying 'WISKI' databases via the 'KiWIS' 'REST' API. 'WISKI' is an 'SQL' relational database 
  used for the collection and storage of water data developed by KISTERS and 'KiWIS' is a 'REST' service that provides
  access to 'WISKI' databases via HTTP requests (<https://water.kisters.de/en/technology-trends/kisters-and-open-data/>). 
  Contains a list of default databases (called 'hubs') and also allows users to provide their own 'KiWIS' URL. 
  Supports the entire query process- from metadata to specific time series values. All data is returned as tidy tibbles.
	"""
	
	homepage = "https://github.com/rywhale/kiwisR"
	cran = "kiwisR" 

	version("0.2.0", md5="5ce41e9500c62a1c0c473e70c8980f7b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
