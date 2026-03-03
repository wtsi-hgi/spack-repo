# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProphet(RPackage):
	"""Automatic Forecasting Procedure

	Implements a procedure for forecasting time series data based on
    an additive model where non-linear trends are fit with yearly, weekly, and
    daily seasonality, plus holiday effects. It works best with time series
    that have strong seasonal effects and several seasons of historical data.
    Prophet is robust to missing data and shifts in the trend, and typically
    handles outliers well.
	"""
	
	homepage = "https://github.com/facebook/prophet"
	cran = "prophet" 

	version("1.0", md5="8df583834d8cb58ebc4cd5421497d9dd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rlang@0.3.0.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7.7:", type=("build", "run"))
	depends_on("r-dygraphs@1.1.1.4:", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-tidyr@0.6.1:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
