# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNortstest(RPackage):
	"""Assessing Normality of Stationary Process

	Despite that several tests for normality in stationary processes have been proposed in the literature, consistent implementations of these tests in programming languages are limited. Seven normality test are implemented. The asymptotic Lobato & Velasco's, asymptotic Epps, Psaradakis and  Vávra, Lobato & Velasco's and Epps sieve bootstrap approximations, El bouch et al., and the random projections tests for univariate stationary process. Some other diagnostics such as, unit root test for  stationarity, seasonal tests for seasonality, and arch effect test for volatility; are also performed. Additionally, the El bouch test performs normality tests for bivariate time series. The package also offers residual diagnostic for linear time series models developed in several packages.
	"""
	
	homepage = "https://github.com/asael697/nortsTest"
	cran = "nortsTest" 

	version("1.1.2", md5="f546896b060d2d04ee8f9d4059e5db12")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-uroot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
