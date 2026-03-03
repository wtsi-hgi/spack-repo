# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIforecast(RPackage):
	"""Machine Learning Time Series Forecasting

	Compute static, onestep and multistep time series forecasts for machine learning models.
	"""
	
	cran = "iForecast" 

	version("1.0.7", md5="40a5a9317045d2f2d030a99112c51efe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
