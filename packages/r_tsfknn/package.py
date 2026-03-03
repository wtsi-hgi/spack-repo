# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsfknn(RPackage):
	"""Time Series Forecasting Using Nearest Neighbors

	Allows forecasting time series using nearest neighbors regression
    Francisco Martinez, Maria P. Frias, Maria D. Perez-Godoy and Antonio J.
    Rivera (2019) <doi:10.1007/s10462-017-9593-z>. When the forecasting horizon
    is higher than 1, two multi-step ahead forecasting strategies can be used.
    The model built is autoregressive, that is, it is only based on the 
    observations of the time series. The nearest neighbors used in a prediction
    can be consulted and plotted.
	"""
	
	homepage = "https://github.com/franciscomartinezdelrio/tsfknn"
	cran = "tsfknn" 

	version("0.6.0", md5="aa04a6c9b9cd1ea8d9d07f31d9170bf6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
