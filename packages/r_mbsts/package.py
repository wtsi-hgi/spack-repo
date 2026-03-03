# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbsts(RPackage):
	"""Multivariate Bayesian Structural Time Series

	Tools for data analysis with multivariate Bayesian structural time series (MBSTS) models.  Specifically, the package provides facilities for implementing general structural time series models, flexibly adding on different time series components (trend, season, cycle, and regression), simulating them, fitting them to multivariate correlated time series data, conducting feature selection on the regression component.
	"""
	
	cran = "mbsts" 

	version("3.0", md5="0db992e0408a62e308eb240b41dc354e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kfas", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
