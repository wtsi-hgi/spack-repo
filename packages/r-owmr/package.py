# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROwmr(RPackage):
	"""OpenWeatherMap API Wrapper

	Accesses OpenWeatherMap's (owm) <https://openweathermap.org/> API.
   'owm' itself is a service providing weather data in the past, in the future and now.
   Furthermore, 'owm' serves weather map layers usable in frameworks like 'leaflet'.
   In order to access the API, you need to sign up for an API key. There are free and paid plans.
   Beside functions for fetching weather data from 'owm', 'owmr' supplies
   tools to tidy up fetched data (for fast and simple access) and to show it on leaflet maps.
	"""
	
	homepage = "https://github.com/crazycapivara/owmr/"
	cran = "owmr" 

	version("0.8.2", md5="1bea3248a7e059baae677ca70f20dade")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
