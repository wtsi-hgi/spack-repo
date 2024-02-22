# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInzightts(RPackage):
	"""Time Series for 'iNZight'

	Provides a collection of functions for working with time series data, including functions for drawing, decomposing, and forecasting. Includes capabilities to compare multiple series and fit both additive and multiplicative models. Used by 'iNZight', a graphical user interface providing easy exploration and visualisation of data for students of statistics, available in both desktop and online versions. Holt (1957) <doi:10.1016/j.ijforecast.2003.09.015>, Winters (1960) <doi:10.1287/mnsc.6.3.324>, Cleveland, Cleveland, & Terpenning (1990) "STL: A Seasonal-Trend Decomposition Procedure Based on Loess".
	"""
	
	homepage = "https://inzight.nz"
	cran = "iNZightTS" 

	version("2.0.0", md5="42db3c9349d7045918b3b7e6c8b48ddc")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-fable", type=("build", "run"))
	depends_on("r-fabletools", type=("build", "run"))
	depends_on("r-feasts", type=("build", "run"))
	depends_on("r-evaluate", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
