# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForecasttb(RPackage):
	"""Test Bench for the Comparison of Forecast Methods

	Provides a test bench for the comparison of forecasting
    methods in uni-variate time series. Forecasting methods are compared using 
    different error metrics. Proposed forecasting methods and alternative error 
    metrics can be used. Detailed discussion is provided in the vignette.
	"""
	
	cran = "ForecastTB" 

	version("1.0.1", md5="43fecc324eb4583eb45bf0a5ed28387c")

	depends_on("r-psf", type=("build", "run"))
	depends_on("r-decomposedpsf", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-imputetestbench", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
