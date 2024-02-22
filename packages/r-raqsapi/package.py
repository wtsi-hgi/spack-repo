# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaqsapi(RPackage):
	"""A Simple Interface to the US EPA Air Quality System Data Mart
API

	Retrieve air monitoring data and associated metadata from the US
  Environmental Protection Agency's Air Quality System service using functions.
  See <https://aqs.epa.gov/aqsweb/documents/data_api.html> for details about
  the US EPA Data Mart API.
	"""
	
	homepage = "<https://github.com/USEPA/RAQSAPI>"
	cran = "RAQSAPI" 

	version("2.0.3", md5="064528cde230d2a96d58c4a5437360c3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
