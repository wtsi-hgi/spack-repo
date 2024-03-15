# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorepls(RPackage):
	"""Interpretation Tools for Partial Least Squares Regression

	Various kinds of plots (observations, variables, correlations, weights, regression coefficients and Variable Importance in the Projection) and aids to interpretation (coefficients, Q2, correlations, redundancies) for partial least squares regressions computed with the 'pls' package, following Tenenhaus (1998, ISBN:2-7108-0735-1).
	"""
	
	cran = "morepls" 

	version("0.1", md5="8e0dac86160e159337a459fe74f22b99")

	depends_on("r-pls", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
