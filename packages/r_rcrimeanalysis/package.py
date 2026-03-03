# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcrimeanalysis(RPackage):
	"""An Implementation of Crime Analysis Methods

	An implementation of functions for the analysis of crime incident or records
  management system data. The package implements analysis algorithms scaled for city
  or regional crime analysis units. The package provides functions for kernel density
  estimation for crime heat maps, geocoding using the 'Google Maps' API, identification 
  of repeat crime incidents, spatio-temporal map comparison across time intervals, 
  time series analysis (forecasting and decomposition), detection of optimal parameters 
  for the identification of near repeat incidents, and near repeat analysis with crime 
  network linkage.
	"""
	
	cran = "rcrimeanalysis" 

	version("0.5.0", md5="f5ec0c1a28a25f8a758668b591388b9c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-leafsync", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-pals", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
