# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArfima(RPackage):
	"""Fractional ARIMA (and Other Long Memory) Time Series Modeling

	Simulates, fits, and predicts long-memory and anti-persistent
	time series, possibly mixed with ARMA, regression, transfer-function
	components.
	Exact methods (MLE, forecasting, simulation) are used.
	Bug reports should be done via GitHub (at
	<https://github.com/JQVeenstra/arfima>), where the development version
	of this package lives; it can be installed using devtools.
	"""
	
	cran = "arfima" 

	version("1.8-1", md5="433c007501f6f38f60670452b2214d4e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ltsa", type=("build", "run"))
