# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNgboostforecast(RPackage):
	"""Probabilistic Time Series Forecasting

	Probabilistic time series forecasting via Natural Gradient Boosting for Probabilistic Prediction.
	"""
	
	homepage = "https://github.com/Akai01/ngboostForecast"
	cran = "ngboostForecast" 

	version("0.1.1", md5="2c3b6f571944050a6304005d8bb7c806")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-reticulate@1.20:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-forecast@8.15:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("python@3.6:", type=("build", "link", "run"))
