# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForecasthybrid(RPackage):
	"""Convenient Functions for Ensemble Time Series Forecasts

	Convenient functions for ensemble forecasts in R combining
    approaches from the 'forecast' package. Forecasts generated from auto.arima(), ets(),
    thetaf(), nnetar(), stlm(), tbats(), and snaive() can be combined with equal weights, weights
    based on in-sample errors (introduced by Bates & Granger (1969) <doi:10.1057/jors.1969.103>),
    or cross-validated weights. Cross validation for time series data with user-supplied models
    and forecasting functions is also supported to evaluate model accuracy.
	"""
	
	homepage = "https://gitlab.com/dashaub/forecastHybrid"
	cran = "forecastHybrid" 

	version("5.0.19", md5="fc14649faad51a75327a46d3a1a48721")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-forecast@8.12:", type=("build", "run"))
	depends_on("r-thief", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-zoo@1.7:", type=("build", "run"))
