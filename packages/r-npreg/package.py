# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpreg(RPackage):
	"""Nonparametric Regression via Smoothing Splines

	Multiple and generalized nonparametric regression using smoothing spline ANOVA models and generalized additive models, as described in Helwig (2020) <doi:10.4135/9781526421036885885>. Includes support for Gaussian and non-Gaussian responses, smoothers for multiple types of predictors (including random intercepts), interactions between smoothers of mixed types, eight different methods for smoothing parameter selection, and flexible tools for diagnostics, inference, and prediction.
	"""
	
	cran = "npreg" 

	version("1.1.0", md5="aaf79ae14844765f05e73f32c6831e94")
	version("1.0-9", md5="4301c7e5626fe34f97024342169b94dc")

