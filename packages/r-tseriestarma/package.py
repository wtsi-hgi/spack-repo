# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTseriestarma(RPackage):
	"""Analysis of Nonlinear Time Series Through TARMA Models

	Routines for nonlinear time series analysis based on Threshold Autoregressive Moving Average models. 
 It provides functions and methods for: TARMA model fitting and forecasting, tests for threshold effects, unit-root tests based on TARMA models.
	"""
	
	cran = "tseriesTARMA" 

	version("0.3-4", md5="58bd2cffd62e27a075e0683c9473a0cd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-lbfgsb3c", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
