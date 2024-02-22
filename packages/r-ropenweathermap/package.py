# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRopenweathermap(RPackage):
	"""R Interface to OpenWeatherMap API

	OpenWeatherMap (OWM) <http://openweathermap.org/api> is a service providing weather related data.
           This package can be used to access current weather data for one location or several locations.
           It can also be used to forecast weather for 5 days with data for every 3 hours.
	"""
	
	cran = "ROpenWeatherMap" 

	version("1.1", md5="5f24c03e26ed5e66590ab0733ccbcb4b")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
