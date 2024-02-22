# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletrf(RPackage):
	"""Wavelet-RF Hybrid Model for Time Series Forecasting

	The Wavelet Decomposition followed by Random Forest Regression (RF) models have been applied for time series forecasting. The maximum overlap discrete wavelet transform (MODWT) algorithm was chosen as it works for any length of the series. The series is first divided into training and testing sets. In each of the wavelet decomposed series, the  supervised machine learning approach namely random forest was employed to train the model. This package also provides accuracy metrics in the form of Root Mean Square Error (RMSE) and Mean Absolute Prediction Error (MAPE). This package is based on the algorithm of Ding et al. (2021) <DOI: 10.1007/s11356-020-12298-3>.
	"""
	
	cran = "WaveletRF" 

	version("0.1.0", md5="e67bcd7a47bfafd33ea3a4a6edb20bb2")

	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-tsutils", type=("build", "run"))
