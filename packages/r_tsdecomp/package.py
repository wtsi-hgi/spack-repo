# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdecomp(RPackage):
	"""Decomposition of Time Series Data

	ARIMA-model-based decomposition of quarterly and 
 monthly time series data.
 The methodology is developed and described, among others, in 
 Burman (1980) <DOI:10.2307/2982132> and 
 Hillmer and Tiao (1982) <DOI:10.2307/2287770>.
	"""
	
	homepage = "https://jalobe.com"
	cran = "tsdecomp" 

	version("0.2", md5="038b09b2ed8a64ebad627893c52b6d77")

	depends_on("r@3:", type=("build", "run"))
