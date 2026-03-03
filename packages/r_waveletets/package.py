# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletets(RPackage):
	"""Wavelet Based Error Trend Seasonality Model

	ETS stands for Error, Trend, and Seasonality, and it is a popular time series forecasting method. Wavelet decomposition can be used for denoising, compression, and feature extraction of signals. By removing the high-frequency components, wavelet decomposition can remove noise from the data while preserving important features. A hybrid Wavelet ETS  (Error Trend-Seasonality) model has been developed for time series forecasting using algorithm of Anjoy and Paul (2017) <DOI:10.1007/s00521-017-3289-9>.
	"""
	
	cran = "WaveletETS" 

	version("0.1.0", md5="203f486b639ee9114df18e6a90fbe6c4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-caretforecast", type=("build", "run"))
