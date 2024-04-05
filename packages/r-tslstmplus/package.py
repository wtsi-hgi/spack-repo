# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTslstmplus(RPackage):
	"""Long-Short Term Memory for Time-Series Forecasting, Enhanced

	The LSTM (Long Short-Term Memory) model is a Recurrent Neural Network (RNN) based architecture that is widely used for time series forecasting. Customizable configurations for the model are allowed, improving the capabilities and usability of this model compared to other packages. This package is based on 'keras' and 'tensorflow' modules and the algorithm of Paul and Garai (2021) <doi:10.1007/s00500-021-06087-4>.
	"""
	
	cran = "TSLSTMplus" 

	version("1.0.4", md5="06f9bca3097acea0c45deeb78887e43f")
	version("1.0.3", md5="9491b895329f43e7330a8b6ee719d6e1")

	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-tsutils", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
