# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletgarch(RPackage):
	"""Fit the Wavelet-GARCH Model to Volatile Time Series Data

	Fits the combination of Wavelet-GARCH model for time series forecasting using algorithm by Paul (2015) <doi:10.3233/MAS-150328>.
	"""
	
	cran = "WaveletGARCH" 

	version("0.1.1", md5="74f1db584cf82438082b3e7620ca22c6")

	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-fints", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
