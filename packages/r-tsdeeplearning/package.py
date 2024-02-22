# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdeeplearning(RPackage):
	"""Deep Learning Model for Time Series Forecasting

	RNNs are preferred for sequential data like time series, speech, text, etc. but when dealing with long range dependencies, vanishing gradient problems account for their poor performance. LSTM and GRU are effective solutions which are nothing but RNN networks with the abilities of learning both short-term and long-term dependencies. Their structural makeup enables them to remember information for a long period without any difficulty. LSTM consists of one cell state and three gates, namely, forget gate, input gate and output gate whereas GRU comprises only two gates, namely, reset gate and update gate. This package consists of three different functions for the application of RNN, LSTM and GRU to any time series data for its forecasting. For method details see Jaiswal, R. et al. (2022). <doi:10.1007/s00521-021-06621-3>. 
	"""
	
	cran = "TSdeeplearning" 

	version("0.1.0", md5="3e49bb20d55e209066b7f5cbb67f46bf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tsutils", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
