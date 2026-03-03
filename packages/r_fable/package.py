# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFable(RPackage):
	"""Forecasting Models for Tidy Time Series

	Provides a collection of commonly used univariate and multivariate
    time series forecasting models including automatically selected exponential 
    smoothing (ETS) and autoregressive integrated moving average (ARIMA) models.
    These models work within the 'fable' framework provided by the 'fabletools'
    package, which provides the tools to evaluate, visualise, and combine models 
    in a workflow consistent with the tidyverse.
	"""
	
	homepage = "https://fable.tidyverts.org"
	cran = "fable" 

	version("0.3.4", md5="200275cbd7998c1beb037819cb99fe40")
	version("0.3.3", md5="c067b6d44dfad5d5d28fef96c9b34be7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-fabletools@0.3:", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tsibble@0.9:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-distributional", type=("build", "run"))
