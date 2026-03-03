# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexor(RPackage):
	"""Flexible Odds Ratio Curves

	Provides flexible hazard ratio curves that enable modeling non-linear relationships between continuous predictors and survival outcomes. This package facilitates a deeper understanding of the impact of each continuous predictor on the outcome by presenting results in terms of odds ratio (OR) curves based on splines. These curves allow for comparison against a specified reference value, aiding in the interpretation of the predictor's effect.
	"""
	
	homepage = "https://github.com/martaaaa/flexOR"
	cran = "flexOR" 

	version("0.9.6", md5="cae8c62dc38462ffa9abaebad6497bfc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
