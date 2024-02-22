# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultibreaker(RPackage):
	"""Tests for a Structural Change in Multivariate Time Series

	Flexible implementation of a structural change point detection algorithm for multivariate time series.
    It authorizes inclusion of trends, exogenous variables, and break test on the intercept or on the full vector autoregression system.
    Bai, Lumsdaine, and Stock (1998) <doi:10.1111/1467-937X.00051>.
	"""
	
	homepage = "https://github.com/loicym/multibreakeR"
	cran = "multibreakeR" 

	version("0.1.0", md5="246a0e98e4836788070437deea41beec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
