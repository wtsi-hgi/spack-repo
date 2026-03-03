# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeteoforecast(RPackage):
	"""Numerical Weather Predictions

	Access to several Numerical Weather Prediction services both in raster format and as a time series for a location. Currently it works with GFS <https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast>, MeteoGalicia <https://www.meteogalicia.gal/web/modelos/threddsIndex.action>, NAM <https://www.ncei.noaa.gov/products/weather-climate-models/north-american-mesoscale>, and RAP <https://www.ncei.noaa.gov/products/weather-climate-models/rapid-refresh-update>.
	"""
	
	homepage = "https://github.com/oscarperpinan/meteoForecast"
	cran = "meteoForecast" 

	version("0.56", md5="7724b0295f0472a59ce86c14f96e72a1")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
