# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REntropy(RPackage):
	"""Estimation of Entropy, Mutual Information and Related Quantities

	Implements various estimators of entropy for discrete random 
  variables, including the shrinkage estimator by Hausser and Strimmer (2009),
  the maximum likelihood and the Millow-Madow estimator, various Bayesian
  estimators, and the Chao-Shen estimator.  It also offers an R interface to the
  NSB estimator.  Furthermore, the package provides functions for estimating the
  Kullback-Leibler divergence, the chi-squared divergence, mutual information,
  and the chi-squared divergence of independence.  It also computes the
  G statistic and the chi-squared statistic and corresponding p-values.
  Furthermore, there are functions for discretizing continuous random variables.
	"""
	
	homepage = "https://strimmerlab.github.io/software/entropy/"
	cran = "entropy" 

	version("1.3.1", md5="a65db89e6e130f8d420d6d3320121bce")

	depends_on("r@3.0.2:", type=("build", "run"))
