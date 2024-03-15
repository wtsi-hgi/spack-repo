# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForecast(RPackage):
	"""Forecasting Functions for Time Series and Linear Models.

	Methods and tools for displaying and analysing univariate time series
	forecasts including exponential smoothing via state space models and
	automatic ARIMA modelling."""

	cran = "forecast"

	license("GPL-3.0-only")

	version("8.22.0", md5="1706f64e99f49ee63b3a2821c3621579")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.2.35:", type=("build", "run"))
