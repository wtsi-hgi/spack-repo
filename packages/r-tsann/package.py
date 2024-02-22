# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsann(RPackage):
	"""Time Series Artificial Neural Network

	The best ANN structure for time series data analysis is a demanding need in the present era.
    This package will find the best-fitted ANN model based on forecasting accuracy.
    The optimum size of the hidden layers was also determined after determining the number of lags to be included.
    This package has been developed using the algorithm of Paul and Garai (2021) <doi:10.1007/s00500-021-06087-4>.
	"""
	
	cran = "TSANN" 

	version("0.1.0", md5="f02949d109ef29f70d9d508f897fdea0")

	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
