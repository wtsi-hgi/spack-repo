# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletann(RPackage):
	"""Wavelet ANN Model

	The wavelet and ANN technique have been combined to reduce the effect of data noise. This wavelet-ANN conjunction model is able to forecast time series data with better accuracy than the traditional time series model. This package fits hybrid Wavelet ANN model for time series forecasting using algorithm by Anjoy and Paul (2017) <DOI: 10.1007/s00521-017-3289-9>.
	"""
	
	cran = "WaveletANN" 

	version("0.1.2", md5="fb79f1bcaff33e1d64fbd8d4cd6fa95c")

	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
