# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletsvr(RPackage):
	"""Wavelet-SVR Hybrid Model for Time Series Forecasting

	The main aim of this package is to combine the advantage of wavelet and support vector machine models for time series forecasting. This package also gives the accuracy measurements in terms of RMSE and MAPE. This package fits the hybrid Wavelet SVR model for time series forecasting The main aim of this package is to combine the advantage of wavelet and Support Vector Regression (SVR) models for time series forecasting. This package also gives the accuracy measurements in terms of Root Mean Square Error (RMSE) and Mean Absolute Prediction Error (MAPE). This package is based on the algorithm of Raimundo and Okamoto (2018) <DOI: 10.1109/INFOCT.2018.8356851>.
	"""
	
	cran = "WaveletSVR" 

	version("0.1.0", md5="fc674829ab98e67fe0ad376c5ca6a76b")

	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-tsutils", type=("build", "run"))
