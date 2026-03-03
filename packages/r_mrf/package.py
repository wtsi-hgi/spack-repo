# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrf(RPackage):
	"""Multiresolution Forecasting

	Forecasting of univariate time series using feature extraction with variable prediction methods is provided. Feature extraction is done with a redundant Haar wavelet transform with filter h = (0.5, 0.5). The advantage of the approach compared to typical Fourier based methods is an dynamic adaptation to varying seasonalities. Currently implemented prediction methods based on the selected wavelets levels and scales are a regression and a multi-layer perceptron. Forecasts can be computed for horizon 1 or higher. Model selection is performed with an evolutionary optimization. Selection criteria are currently the AIC criterion, the Mean Absolute Error or the Mean Root Error. The data is split into three parts for model selection: Training, test, and evaluation dataset. The training data is for computing the weights of a parameter set. The test data is for choosing the best parameter set. The evaluation data is for assessing the forecast performance of the best parameter set on new data unknown to the model. This work is published in Stier, Q.; Gehlert, T.; Thrun, M.C. Multiresolution Forecasting for Industrial Applications. Processes 2021, 9, 1697. <doi:10.3390/pr9101697>.
	"""
	
	homepage = "https://www.deepbionics.org"
	cran = "mrf" 

	version("0.1.6", md5="8de0482d783e138d230f9a4c126a709e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-monmlp", type=("build", "run"))
	depends_on("r-nnfor", type=("build", "run"))
