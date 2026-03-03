# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletlstm(RPackage):
	"""Wavelet Based LSTM Model

	A wavelet-based LSTM model is a type of neural network architecture that uses wavelet technique to pre-process the input data before passing it through a Long Short-Term Memory (LSTM) network. The wavelet-based LSTM model is a powerful approach that combines the benefits of wavelet analysis and LSTM networks to improve the accuracy of predictions in various applications. This package has been developed using the algorithm of Anjoy and Paul (2017) and Paul and Garai (2021) <DOI:10.1007/s00521-017-3289-9> <doi:10.1007/s00500-021-06087-4>.
	"""
	
	cran = "WaveletLSTM" 

	version("0.1.0", md5="10a03aa0ad4adbfb6f88e57577c0d2c4")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caretforecast", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-tslstm", type=("build", "run"))
