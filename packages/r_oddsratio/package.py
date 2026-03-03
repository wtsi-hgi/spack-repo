# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROddsratio(RPackage):
	"""Odds Ratio Calculation for GAM(M)s & GLM(M)s

	Simplified odds ratio calculation of GAM(M)s &
    GLM(M)s. Provides structured output (data frame) of all predictors and
    their corresponding odds ratios and confident intervals for further
    analyses.  It helps to avoid false references of predictors and
    increments by specifying these parameters in a list instead of using
    'exp(coef(model))' (standard approach of odds ratio calculation for
    GLMs) which just returns a plain numeric output.  For GAM(M)s, odds
    ratio calculation is highly simplified with this package since it
    takes care of the multiple 'predict()' calls of the chosen predictor
    while holding other predictors constant. Also, this package allows
    odds ratio calculation of percentage steps across the whole predictor
    distribution range for GAM(M)s.  In both cases, confident intervals
    are returned additionally. Calculated odds ratio of GAM(M)s can be
    inserted into the smooth function plot.
	"""
	
	homepage = "https://github.com/pat-s/oddsratio"
	cran = "oddsratio" 

	version("2.0.1", md5="2c7025f430b2257f8972d11a407cc6cd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
