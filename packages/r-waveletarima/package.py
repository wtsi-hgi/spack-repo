# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletarima(RPackage):
	"""Wavelet-ARIMA Model for Time Series Forecasting

	Noise in the time-series data significantly affects the accuracy of the ARIMA model. Wavelet transformation decomposes the time series data into subcomponents to reduce the noise and help to improve the model performance. The wavelet-ARIMA model can achieve higher prediction accuracy than the traditional ARIMA model. This package provides Wavelet-ARIMA model for time series forecasting based on the algorithm by Aminghafari and Poggi (2012) and Paul and Anjoy (2018) <doi:10.1142/S0219691307002002> <doi:10.1007/s00704-017-2271-x>.
	"""
	
	cran = "WaveletArima" 

	version("0.1.2", md5="9aefe843bb03b1030740c9c8a4dd5be4")

	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
