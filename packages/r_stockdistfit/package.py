# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStockdistfit(RPackage):
	"""Fit Stock Price Distributions

	The 'StockDistFit' package provides functions for fitting probability distributions to stock price data. The package uses maximum likelihood estimation to find the best-fitting distribution for a given stock. It also offers a function to fit several distributions to one or more assets and compare the distribution with the Akaike Information Criterion (AIC) and then pick the best distribution. References are as follows: Siew et al. (2008) <https://www.jstage.jst.go.jp/article/jappstat/37/1/37_1_1/_pdf/-char/ja> and Benth et al. (2008) <https://books.google.co.ke/books?hl=en&lr=&id=MHNpDQAAQBAJ&oi=fnd&pg=PR7&dq=Stochastic+modeling+of+commodity+prices+using+the+Variance+Gamma+(VG)+model.+&ots=YNIL2QmEYg&sig=XZtGU0lp4oqXHVyPZ-O8x5i7N3w&redir_esc=y#v=onepage&q&f=false>.
	"""
	
	cran = "StockDistFit" 

	version("1.0.0", md5="b11da1a11f1a099ee912fdd08e3be481")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-ghyp", type=("build", "run"))
