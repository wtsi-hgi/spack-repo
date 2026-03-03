# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSci(RPackage):
	"""Standardized Climate Indices Such as SPI, SRI or SPEI

	Functions for generating Standardized Climate Indices (SCI). 
		SCI is a transformation of (smoothed) climate (or environmental)
		time series that  removes seasonality and forces the data to
		take values of the standard normal distribution. SCI was 
		originally developed for precipitation. In this case it is 
		known as the Standardized Precipitation Index (SPI).
	"""
	
	cran = "SCI" 

	version("1.0-2", md5="a0c32b82f5c6588859c1d7aa3fc5fc2e")

	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-lmomco", type=("build", "run"))
