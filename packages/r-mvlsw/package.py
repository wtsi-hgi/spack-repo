# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvlsw(RPackage):
	"""Multivariate, Locally Stationary Wavelet Process Estimation

	Tools for analysing multivariate time series with wavelets. This includes: simulation of a multivariate locally stationary wavelet (mvLSW) process from a multivariate evolutionary wavelet spectrum (mvEWS); estimation of the mvEWS, local coherence and local partial coherence. See Park, Eckley and Ombao (2014) <doi:10.1109/TSP.2014.2343937> for details.
	"""
	
	cran = "mvLSW" 

	version("1.2.5", md5="8ed754550177480f3bbc3f55eb4650dd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
