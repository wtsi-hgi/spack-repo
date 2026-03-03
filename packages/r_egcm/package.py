# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgcm(RPackage):
	"""Engle-Granger Cointegration Models

	An easy-to-use implementation of the Engle-Granger
  two-step procedure for identifying pairs of cointegrated series.  It is
  geared towards the analysis of pairs of securities.  Summary and plot
  functions are provided, and the package is able to fetch closing prices of
  securities from Yahoo.  A variety of unit root tests are supported, and 
  an improved unit root test is included.  
	"""
	
	cran = "egcm" 

	version("1.0.13", md5="66db8663b822fe2976e605bdb8061a4d")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
