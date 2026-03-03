# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArimaann(RPackage):
	"""Time Series Forecasting using ARIMA-ANN Hybrid Model

	Testing, Implementation, and Forecasting of the ARIMA-ANN hybrid model. The ARIMA-ANN hybrid model combines the distinct strengths of the Auto-Regressive Integrated Moving Average (ARIMA) model and the Artificial Neural Network (ANN) model for time series forecasting.For method details see Zhang, GP (2003) <doi:10.1016/S0925-2312(01)00702-0>.
	"""
	
	cran = "ARIMAANN" 

	version("0.1.0", md5="2f5eefc985f8d7bcadcfdab2c06b674e")

	depends_on("r@2.3.1:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
