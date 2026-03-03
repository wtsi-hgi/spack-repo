# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwunderground(RPackage):
	"""R Interface to Weather Underground API

	Tools for getting historical weather information and forecasts 
    from wunderground.com. Historical weather and forecast data includes, but 
    is not limited to, temperature, humidity, windchill, wind speed, dew point, 
    heat index. Additionally, the weather underground weather API also includes 
    information on sunrise/sunset, tidal conditions, satellite/webcam imagery, 
    weather alerts, hurricane alerts and historical high/low temperatures.
	"""
	
	homepage = "https://github.com/ALShum/rwunderground"
	cran = "rwunderground" 

	version("0.1.8", md5="835a012a9b364555b834994e0c08d29f")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
