# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForecastsnsts(RPackage):
	"""Forecasting for Stationary and Non-Stationary Time Series

	Methods to compute linear h-step ahead prediction coefficients based
    on localised and iterated Yule-Walker estimates and empirical mean squared
    and absolute prediction errors for the resulting predictors. Also, functions
    to compute autocovariances for AR(p) processes, to simulate tvARMA(p,q) time
    series, and to verify an assumption from Kley et al. (2019), Electronic of Statistics,
    forthcoming. Preprint <arXiv:1611.04460>.
	"""
	
	homepage = "http://github.com/tobiaskley/forecastSNSTS"
	cran = "forecastSNSTS" 

	version("1.3-0", md5="fe87f9eb8da4a4715fb3a2241f0ac173")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
