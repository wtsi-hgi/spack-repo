# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStocks(RPackage):
	"""Stock Market Analysis

	Functions for analyzing stocks or other investments. Main features are loading and aligning historical data for ticker symbols, calculating performance metrics for individual funds or portfolios (e.g. annualized growth, maximum drawdown, Sharpe/Sortino ratio), and creating graphs. C++ code is used to improve processing speed where possible.
	"""
	
	cran = "stocks" 

	version("1.1.4", md5="318f194ebd9c2dceea68d7e870072222")

	depends_on("r-rbenchmark", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-dvmisc", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
