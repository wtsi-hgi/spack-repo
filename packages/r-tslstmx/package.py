# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTslstmx(RPackage):
	"""Predict Time Series Using LSTM Model Including Exogenous
Variable to Denote Zero Values

	It is a versatile tool for predicting time series data using Long Short-Term Memory (LSTM) models. It is specifically designed to handle time series with an exogenous variable, allowing users to denote whether data was available for a particular period or not. The package encompasses various functionalities, including hyperparameter tuning, custom loss function support, model evaluation, and one-step-ahead forecasting. With an emphasis on ease of use and flexibility, it empowers users to explore, evaluate, and deploy LSTM models for accurate time series predictions and forecasting in diverse applications. More details can be found in Garai and Paul (2023) <doi:10.1016/j.iswa.2023.200202>.
	"""
	
	cran = "tsLSTMx" 

	version("0.1.0", md5="adad67a3b38f5640589046dff32e7db2")

	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-allmetrics", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
