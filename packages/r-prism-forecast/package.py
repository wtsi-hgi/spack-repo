# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrismForecast(RPackage):
	"""Penalized Regression with Inferred Seasonality Module -
Forecasting Unemployment Initial Claims using 'Google Trends'
Data

	Implements Penalized Regression with Inferred Seasonality Module (PRISM) to generate forecast estimation of weekly unemployment initial claims using 'Google Trends' data. It includes required data and tools for backtesting the performance in 2007-2020.
	"""
	
	homepage = "https://github.com/ryanddyi/prism"
	cran = "PRISM.forecast" 

	version("0.2.1", md5="81e0b3f81fe9b1d1efe58c0dbaabef14")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
