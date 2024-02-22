# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRclimacell(RPackage):
	"""R Wrapper for the 'Climacell' API

	'Climacell' is a weather platform that provides hyper-local forecasts and weather 
    data. This package enables the user to query the core layers of the 
    time line interface of the 'Climacell' v4 API <https://www.climacell.co/weather-api/>. 
    This package requires a valid API key. See vignettes for instructions on use.
	"""
	
	homepage = "https://nikdata.github.io/RClimacell/"
	cran = "RClimacell" 

	version("0.1.4", md5="cd1b4ae4343074faef4d01b9f19dc876")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.6:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
