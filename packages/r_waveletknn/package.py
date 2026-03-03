# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletknn(RPackage):
	"""Wavelet Based K-Nearest Neighbor Model

	The employment of the Wavelet decomposition technique proves to be highly advantageous in the modelling of noisy time series data. Wavelet decomposition technique using the "haar" algorithm has been incorporated to formulate a hybrid Wavelet KNN (K-Nearest Neighbour) model for time series forecasting, as proposed by Anjoy and Paul (2017) <DOI:10.1007/s00521-017-3289-9>.
	"""
	
	cran = "WaveletKNN" 

	version("0.1.0", md5="46f7d6facca6f93eab8889f079aafb36")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caretforecast", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-wavelets", type=("build", "run"))
