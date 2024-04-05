# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapa(RPackage):
	"""Multiple Aggregation Prediction Algorithm

	Functions and wrappers for using the Multiple Aggregation Prediction Algorithm (MAPA) for time series forecasting. MAPA models and forecasts time series at multiple temporal aggregation levels, thus strengthening and attenuating the various time series components for better holistic estimation of its structure. For details see Kourentzes et al. (2014) <doi:10.1016/j.ijforecast.2013.09.006>.
	"""
	
	homepage = "https://kourentzes.com/forecasting/2014/04/19/multiple-aggregation-prediction-algorithm-mapa/"
	cran = "MAPA" 

	version("2.0.7", md5="485879ee312d84c34ea66cc4a8d5e704")
	version("2.0.6", md5="188108741c135acf983954efaec0aa41")

	depends_on("r-forecast@5.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-smooth@4:", type=("build", "run"))
