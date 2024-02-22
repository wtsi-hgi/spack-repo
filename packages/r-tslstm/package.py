# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTslstm(RPackage):
	"""Long Short Term Memory (LSTM) Model for Time Series Forecasting

	The LSTM (Long Short-Term Memory) model is a Recurrent Neural Network (RNN) based architecture that is widely used for time series forecasting. Min-Max transformation has been used for data preparation. Here, we have used one LSTM layer as a simple LSTM model and a Dense layer is used as the output layer. Then, compile the model using the loss function, optimizer and metrics. This package is based on Keras and TensorFlow modules and the algorithm of Paul and Garai (2021) <doi:10.1007/s00500-021-06087-4>.
	"""
	
	cran = "TSLSTM" 

	version("0.1.0", md5="7b6cb6f1850a9b8b715dc009a57eae6b")

	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-tsutils", type=("build", "run"))
