# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvdisc(RPackage):
	"""Discrete Time Survival and Longitudinal Data Analysis

	Various functions for discrete time survival analysis and longitudinal analysis. SIMEX method for correcting for bias for errors-in-variables
  in a mixed effects model. Asymptotic mean and variance of different proportional hazards test statistics using different ties methods given two
  survival curves and censoring distributions. Score test and Wald test for regression analysis of grouped survival data. Calculation of survival
  curves for events defined by the response variable in a mixed effects model crossing a threshold with or without confirmation.
	"""
	
	cran = "SurvDisc" 

	version("0.1.1", md5="aacfea06e63a8c3409e18236c2278eae")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-simex", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
