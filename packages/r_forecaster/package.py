# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForecaster(RPackage):
	"""Time Series Forecast System

	A web application for displaying, analysing and forecasting univariate time series. Includes basic methods such as mean, naïve, seasonal naïve and drift, as well as more complex methods such as Holt-Winters Box,G and Jenkins, G (1976) <doi:10.1111/jtsa.12194> and ARIMA Brockwell, P.J. and R.A.Davis (1991) <doi:10.1007/978-1-4419-0320-4>.
	"""
	
	homepage = "https://promidat.website"
	cran = "forecasteR" 

	version("2.0.2", md5="b99406e95eee492b67f8f62fd0c1e9e0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-echarts4r", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-shinycustomloader", type=("build", "run"))
	depends_on("r-shinydashboardplus@2:", type=("build", "run"))
