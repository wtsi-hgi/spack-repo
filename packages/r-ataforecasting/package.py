# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtaforecasting(RPackage):
	"""Automatic Time Series Analysis and Forecasting using the Ata
Method

	The Ata method (Yapar et al. (2019) <doi:10.15672/hujms.461032>), an alternative to exponential smoothing (described in Yapar (2016) <doi:10.15672/HJMS.201614320580>,
	Yapar et al. (2017) <doi:10.15672/HJMS.2017.493>), is a new univariate time series forecasting method which provides innovative solutions to issues faced during the
	initialization and optimization stages of existing forecasting methods. Forecasting performance of the Ata method is superior to existing methods both in terms of easy
	implementation and accurate forecasting. It can be applied to non-seasonal or seasonal time series which can be decomposed into four components (remainder, level, trend
	and seasonal). This methodology performed well on the M3 and M4-competition data. This package was written based on Ali Sabri Taylan’s PhD dissertation.
	"""
	
	homepage = "https://github.com/alsabtay/ATAforecasting"
	cran = "ATAforecasting" 

	version("0.0.60", md5="0a9b2830c164c130c1c0c036afd0fc4d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-seasonal", type=("build", "run"))
	depends_on("r-stlplus", type=("build", "run"))
	depends_on("r-str", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-tsa", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
