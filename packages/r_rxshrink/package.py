# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRxshrink(RPackage):
	"""Maximum Likelihood Shrinkage using Generalized Ridge or Least
Angle Regression

	Functions are provided to calculate and display ridge TRACE Diagnostics for a 
  variety of alternative Shrinkage Paths. While all methods focus on Maximum Likelihood 
  estimation of unknown true effects under normal distribution-theory, some estimates are 
  modified to be Unbiased or to have "Correct Range" when estimating either [1] the noncentrality 
  of the F-ratio for testing that true Beta coefficients are Zeros or [2] the "relative" MSE 
  Risk (i.e. MSE divided by true sigma-square, where the "relative" variance of OLS is known.) 
  The eff.ridge() function implements the "Efficient Shrinkage Path" introduced in Obenchain
  (2022) <Open Statistics>. This "p-Parameter" Shrinkage-Path always passes through the
  vector of regression coefficient estimates Most-Likely to achieve the overall Optimal
  Variance-Bias Trade-Off and is the shortest Path with this property. Functions eff.aug() and
  eff.biv() augment the calculations made by eff.ridge() to provide plots of the bivariate
  confidence ellipses corresponding to any of the p*(p-1) possible ordered pairs of shrunken
  regression coefficients. Functions for plotting TRACE Diagnostics now have more options. 
	"""
	
	homepage = "https://www.R-project.org"
	cran = "RXshrink" 

	version("2.3", md5="638cbf02caea69a4c3e46b64905fd8c5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
