# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtsa(RPackage):
	"""Alternative Time Series Analysis

	Contains some tools for testing, analyzing time series data and
    fitting popular time series models such as ARIMA, Moving Average and Holt
    Winters, etc. Most functions also provide nice and clear outputs like SAS
    does, such as identify, estimate and forecast, which are the same statements
    in PROC ARIMA in SAS.
	"""
	
	cran = "aTSA" 

	version("3.1.2.1", md5="7bee1f397b1605e9754d31463085a0ae")

