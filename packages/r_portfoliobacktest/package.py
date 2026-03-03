# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortfoliobacktest(RPackage):
	"""Automated Backtesting of Portfolios over Multiple Datasets

	Automated backtesting of multiple portfolios over multiple 
    datasets of stock prices in a rolling-window fashion. Intended for 
    researchers and practitioners to backtest a set of different portfolios, 
    as well as by a course instructor to assess the students in their portfolio 
    design in a fully automated and convenient manner, with results conveniently 
    formatted in tables and plots. Each portfolio design is easily defined as a
    function that takes as input a window of the stock prices and outputs the 
    portfolio weights. Multiple portfolios can be easily specified as a list 
    of functions or as files in a folder. Multiple datasets can be conveniently 
    extracted randomly from different markets, different time periods, and 
    different subsets of the stock universe. The results can be later assessed 
    and ranked with tables based on a number of performance criteria (e.g., 
    expected return, volatility, Sharpe ratio, drawdown, turnover rate, return 
    on investment, computational time, etc.), as well as plotted in a number of 
    ways with nice barplots and boxplots.
	"""
	
	homepage = "https://CRAN.R-project.org/package=portfolioBacktest"
	cran = "portfolioBacktest" 

	version("0.4.1", md5="6168e2f0c76424b812db61c9d08cc75e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-evaluate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
