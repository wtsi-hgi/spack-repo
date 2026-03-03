# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpregfast(RPackage):
	"""Nonparametric Estimation of Regression Models with
Factor-by-Curve Interactions

	A method for obtaining nonparametric estimates of regression models
    with or without factor-by-curve interactions using local polynomial kernel
    smoothers or splines. Additionally, a parametric model (allometric model) can be
    estimated.
	"""
	
	cran = "npregfast" 

	version("1.5.2", md5="f0200e7af391e2e46b77870a94619ffb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-wesanderson", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
