# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootwptos(RPackage):
	"""Test Stationarity using Bootstrap Wavelet Packet Tests

	Provides significance tests for second-order stationarity
	for time series using bootstrap wavelet packet tests.
	Provides functionality to visualize the time series with
	the results of the hypothesis tests superimposed.
	The methodology is described in Cardinali, A and Nason, G P (2016)
	"Practical powerful wavelet packet tests for second-order stationarity."
	Applied and Computational Harmonic Analysis, 44, 558-585
	<doi:10.1016/j.acha.2016.06.006>.
	"""
	
	cran = "BootWPTOS" 

	version("1.2.1", md5="592b961cdd5b119a0036e77a8b333998")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
