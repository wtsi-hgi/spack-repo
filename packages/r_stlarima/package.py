# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStlarima(RPackage):
	"""STL Decomposition and ARIMA Hybrid Forecasting Model

	Univariate time series forecasting with STL decomposition based auto regressive integrated moving average (ARIMA) hybrid  model. For method details see Xiong T, Li C, Bao Y (2018). <doi:10.1016/j.neucom.2017.11.053>. 
	"""
	
	cran = "stlARIMA" 

	version("0.1.0", md5="ded248b2dd334d9f5c06590415c3bad6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
