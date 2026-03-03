# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletgbm(RPackage):
	"""Wavelet Based Gradient Boosting Method

	Wavelet decomposition method is very useful for modelling noisy time series data. Wavelet decomposition using 'haar' algorithm has been implemented to developed hybrid Wavelet GBM (Gradient Boosting Method) model for time series forecasting using algorithm by Anjoy and Paul (2017) <DOI:10.1007/s00521-017-3289-9>.
	"""
	
	cran = "WaveletGBM" 

	version("0.1.0", md5="3ce18e19f51fab1aa3d73b4088907489")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caretforecast", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
