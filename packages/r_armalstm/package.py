# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArmalstm(RPackage):
	"""Fitting of Hybrid ARMA-LSTM Models

	The real-life time series data are hardly pure linear or nonlinear. Merging a linear time series model like the autoregressive moving average (ARMA) model with a nonlinear neural network model such as the Long Short-Term Memory (LSTM) model can be used as a hybrid model for more accurate modeling purposes. Both the autoregressive integrated moving average (ARIMA) and autoregressive fractionally integrated moving average (ARFIMA) models can be implemented. Details can be found in Box et al. (2015, ISBN: 978-1-118-67502-1) and Hochreiter and Schmidhuber (1997) <doi:10.1162/neco.1997.9.8.1735>.
	"""
	
	cran = "ARMALSTM" 

	version("0.1.0", md5="a7d6b6f46d0254d4a51fd68ade01b7f5")

	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
