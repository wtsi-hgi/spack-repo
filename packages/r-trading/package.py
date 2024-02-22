# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrading(RPackage):
	"""CCR, Advanced Correlation & Beta Estimates, Betting Strategies

	Contains performance analysis metrics of track records including entropy-based
            correlation and dynamic beta based on the Kalman filter. The normalized sample entropy method
            has been implemented which produces accurate entropy estimation even on smaller datasets while for
            the dynamic beta calculation the Kalman filter methodology has been utilized.
            On a separate stream, trades from the five major assets classes and also
            functionality to use pricing curves, rating tables, CSAs and add-on tables. The
            implementation follows an object oriented logic whereby each trade inherits from
            more abstract classes while also the curves/tables are objects. Furthermore, odds calculators
            and P&L back-testing functionality has been implemented for the most widely used betting/trading
            strategies including martingale, DAlembert, Labouchere and Fibonacci. Back-testing has also been included for the EuroMillions and EuroJackpot lotteries.
			Furthermore, some basic functionality about climate risk has been included. 
	"""
	
	homepage = "https://openriskcalculator.com/"
	cran = "Trading" 

	version("3.0", md5="efd3898d509b99c43bc2e45040c9ea0e")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rcppalgos", type=("build", "run"))
