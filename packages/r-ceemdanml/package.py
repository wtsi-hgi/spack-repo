# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeemdanml(RPackage):
	"""CEEMDAN Decomposition Based Hybrid Machine Learning Models

	Noise in the time-series data significantly affects the accuracy of the Machine Learning (ML) models (Artificial Neural Network and Support Vector Regression are considered here). Complete Ensemble Empirical Mode Decomposition with Adaptive Noise (CEEMDAN) decomposes the time series data into sub-series and help to improve the model performance. The models can achieve higher prediction accuracy than the traditional ML models. Two models have been provided here for time series forecasting. More information may be obtained from Garai and Paul (2023) <doi:10.1016/j.iswa.2023.200202>.
	"""
	
	cran = "CEEMDANML" 

	version("0.1.0", md5="78d443f22f055d90c48d1cf40266a2dd")

	depends_on("r-rlibeemd", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-atsa", type=("build", "run"))
	depends_on("r-fints", type=("build", "run"))
	depends_on("r-lsts", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
