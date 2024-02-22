# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcademictwitter(RPackage):
	"""Access the Twitter Academic Research Product Track V2 API
Endpoint

	Package to query the Twitter Academic Research Product Track,
    providing access to full-archive search and other v2 API endpoints. Functions
    are written with academic research in mind. They provide flexibility in how 
    the user wishes to store collected data, and encourage regular storage of data
    to mitigate loss when collecting large volumes of tweets. They also provide
    workarounds to manage and reshape the format in which data is provided on
    the client side.
	"""
	
	homepage = "https://github.com/cjbarrie/academictwitteR"
	cran = "academictwitteR" 

	version("0.3.1", md5="d2369159065fbbd52f1f89ef085a3c71")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
