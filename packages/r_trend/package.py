# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrend(RPackage):
	"""Non-Parametric Trend Tests and Change-Point Detection

	The analysis of environmental data often requires
	     the detection of trends and change-points. 
	     This package includes tests for trend detection
	     (Cox-Stuart Trend Test, Mann-Kendall Trend Test, 
	     (correlated) Hirsch-Slack Test,
             partial Mann-Kendall Trend Test, multivariate (multisite)
	     Mann-Kendall Trend Test, (Seasonal) Sen's slope, 
	     partial Pearson and Spearman correlation trend test),
             change-point detection (Lanzante's test procedures, 
	     Pettitt's test, Buishand Range Test,
	     Buishand U Test, Standard Normal Homogeinity Test),
	     detection of non-randomness (Wallis-Moore Phase Frequency Test,
	     Bartels rank von Neumann's ratio test, Wald-Wolfowitz Test)
	     and the two sample Robust Rank-Order Distributional Test.
	"""
	
	cran = "trend" 

	version("1.1.6", md5="ed2527477d16293a052d031ad9ee21c2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-extradistr@1.8:", type=("build", "run"))
