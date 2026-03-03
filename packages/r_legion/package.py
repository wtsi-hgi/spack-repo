# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLegion(RPackage):
	"""Forecasting Using Multivariate Models

	Functions implementing multivariate state space models for purposes of time series analysis and forecasting.
             The focus of the package is on multivariate models, such as Vector Exponential Smoothing,
             Vector ETS (Error-Trend-Seasonal model) etc. It currently includes Vector Exponential
             Smoothing (VES, de Silva et al., 2010, <doi:10.1177/1471082X0901000401>), Vector ETS and
             simulation function for VES.
	"""
	
	homepage = "https://github.com/config-i1/legion"
	cran = "legion" 

	version("0.1.2", md5="d951afa1ebb47fbc364e9b3084fa1d50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-greybox@1.0.4:", type=("build", "run"))
	depends_on("r-smooth@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.8.100:", type=("build", "run"))
