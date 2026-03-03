# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwind(RPackage):
	"""Download, Edit and Include Wind and Sea Currents Data in
Ecological and Evolutionary Analysis

	Tools for download and manage surface wind and sea currents data from the Global Forecasting System <https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast> and to compute connectivity between locations.
	"""
	
	homepage = "http://allthiswasfield.blogspot.com.es/"
	cran = "rWind" 

	version("1.1.7", md5="7e2428dddc5f7fb1a8aa13f707aab8c1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-raster@2.5.8:", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
