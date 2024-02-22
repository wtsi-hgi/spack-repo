# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeasonalityplot(RPackage):
	"""Seasonality Variation Plots of Stock Prices and Cryptocurrencies

	The price action at any given time is determined by investor 
  sentiment and market conditions. Although there is no established principle, 
  over a long period of time, things often move with a certain periodicity.
  This is sometimes referred to as anomaly. 
  The seasonPlot() function in this package calculates and visualizes the 
  average value of price movements over a year for any given period. 
  In addition, the monthly increase or decrease in price movement is 
  represented with a colored background. 
  This seasonPlot() function can use the same symbols as the 'quantmod' package 
  (e.g. ^IXIC, ^DJI, SPY, BTC-USD, and ETH-USD etc). 
	"""
	
	homepage = "https://github.com/kumeS/seasonalityPlot"
	cran = "seasonalityPlot" 

	version("1.2.1", md5="c8dcef769d3da989ab673964cfc85e0b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-crypto2", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
