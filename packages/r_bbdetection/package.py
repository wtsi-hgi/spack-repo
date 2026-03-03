# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbdetection(RPackage):
	"""Identification of Bull and Bear States of the Market

	Implements two algorithms of detecting Bull and Bear markets in stock prices: the algorithm of Pagan and Sossounov (2002, <doi:10.1002/jae.664>) and the algorithm of Lunde and Timmermann (2004, <doi:10.1198/073500104000000136>).  
       The package also contains functions for printing out the dating of the Bull and Bear states of the market, the descriptive statistics of the states, and functions for plotting the results. 
       For the sake of convenience, the package includes the monthly and daily data on the prices (not adjusted for dividends) of the S&P 500 stock market index.
	"""
	
	cran = "bbdetection" 

	version("1.0", md5="dd2db05ea076abfc707dbf6fd98c90ea")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
