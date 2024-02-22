# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtl(RPackage):
	"""Risk Tool Library - Trading, Risk, 'Analytics' for Commodities

	A toolkit for Commodities 'analytics', risk management and
    trading professionals. Includes functions for API calls to
    <https://commodities.morningstar.com/#/>, <https://developer.genscape.com/>,
    and <https://www.bankofcanada.ca/valet/docs>.
	"""
	
	homepage = "https://github.com/risktoollib/RTL"
	cran = "RTL" 

	version("1.3.5", md5="cbc7f5e9bd9b07da56970a3dd1fb3b72")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-timetk", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
