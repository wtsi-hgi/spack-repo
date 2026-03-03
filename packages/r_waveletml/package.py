# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletml(RPackage):
	"""Wavelet Decomposition Based Hybrid Machine Learning Models

	Wavelet decomposes a series into multiple sub series called detailed and smooth components which helps to capture volatility at multi resolution level by various models. Two hybrid Machine Learning (ML) models (Artificial Neural Network and Support Vector Regression have been used) have been developed in combination with stochastic models, feature selection, and optimization algorithms for prediction of the data. The algorithms have been developed following Paul and Garai (2021)  <doi:10.1007/s00500-021-06087-4>. 
	"""
	
	cran = "WaveletML" 

	version("0.1.0", md5="0b0e5c82ce70d2f81a1a95e8c1ea1028")

	depends_on("r-wavelets", type=("build", "run"))
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
