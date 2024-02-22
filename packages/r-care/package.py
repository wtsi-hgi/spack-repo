# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCare(RPackage):
	"""High-Dimensional Regression and CAR Score Variable Selection

	Implements the regression approach 
  of Zuber and Strimmer (2011) "High-dimensional regression and variable 
  selection using CAR scores" SAGMB 10: 34, <DOI:10.2202/1544-6115.1730>.
  CAR scores measure the correlation between the response and the 
  Mahalanobis-decorrelated  predictors.  The squared CAR score is a 
  natural measure of variable importance and provides a canonical 
  ordering of variables. This package provides functions for estimating 
  CAR scores, for variable selection using CAR scores, and for estimating 
  corresponding regression coefficients. Both shrinkage as well as 
  empirical estimators are available.
	"""
	
	homepage = "https://strimmerlab.github.io/software/care/"
	cran = "care" 

	version("1.1.11", md5="f9cb6dbb1e8053e034bb20637ed0d333")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-corpcor@1.6.10:", type=("build", "run"))
