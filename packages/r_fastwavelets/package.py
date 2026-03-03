# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastwavelets(RPackage):
	"""Compute Maximal Overlap Discrete Wavelet Transform (MODWT) and À
Trous Discrete Wavelet Transform

	A lightweight package to compute Maximal Overlap Discrete Wavelet 
    Transform (MODWT) and À Trous Discrete Wavelet Transform by leveraging the 
    power of 'Rcpp' to make these operations fast. This package was designed for use in forecasting, and
    allows users avoid the inclusion of future data when performing wavelet decomposition of time series.
    See Quilty and Adamowski (2018) <doi:10.1016/j.jhydrol.2018.05.003>.
	"""
	
	homepage = "https://github.com/johnswyou/fastWavelets"
	cran = "fastWavelets" 

	version("1.0.1", md5="969f220bb15cb51069923a9373e80d0a")

	depends_on("r-rcpp", type=("build", "run"))
