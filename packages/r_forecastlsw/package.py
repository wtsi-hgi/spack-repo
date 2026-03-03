# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForecastlsw(RPackage):
	"""Forecasting Routines for Locally Stationary Wavelet Processes

	Implementation to perform forecasting of locally stationary wavelet processes by examining the local second order structure of the time series. 
	"""
	
	cran = "forecastLSW" 

	version("1.0", md5="86dfb4f88030e0dd34224bf6a4c08343")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-locits", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-lpacf", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
