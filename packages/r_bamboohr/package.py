# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBamboohr(RPackage):
	"""A Wrapper to the 'BambooHR' API

	Enables a user to consume the 'BambooHR' API endpoints using R. The
  actual URL of the API will depend on your company domain, and will be handled
  by the package automatically once you setup the config file. The API documentation
  can be found here <https://documentation.bamboohr.com/docs>.
	"""
	
	homepage = "https://mangothecat.github.io/bambooHR/"
	cran = "bambooHR" 

	version("0.1.1", md5="c92eb5dc89dc0730a6c61cde02a09830")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
