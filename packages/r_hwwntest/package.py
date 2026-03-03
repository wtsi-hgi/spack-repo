# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHwwntest(RPackage):
	"""Tests of White Noise using Wavelets

	Provides methods to test whether time series is consistent
	with white noise. Two new tests based on Haar wavelets and general
	wavelets described by Nason and Savchev (2014)
	<doi:10.1002/sta4.69> are provided and, for comparison purposes
	this package also implements the
	B test of Bartlett (1967) <doi:10.2307/2333850>. Functionality
	is provided to compute an approximation to the theoretical
	power of the general wavelet test in the case of general
	ARMA alternatives.
	"""
	
	cran = "hwwntest" 

	version("1.3.2", md5="bfa42677de709fe8f372c78bddaab398")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
