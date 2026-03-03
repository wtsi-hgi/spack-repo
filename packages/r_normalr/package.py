# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormalr(RPackage):
	"""Normalisation of Multiple Variables in Large-Scale Datasets

	The robustness of many of the statistical techniques, such as factor analysis, applied in 
          the social sciences rests upon the assumption of item-level normality. However, when dealing 
          with real data, these assumptions are often not met. The Box-Cox transformation (Box & Cox, 1964)
          <http://www.jstor.org/stable/2984418> provides an optimal transformation for non-normal variables. Yet, for 
          large datasets of continuous variables, its application in current software programs is cumbersome
          with analysts having to take several steps to normalise each variable. We present an R package 
          'normalr' that enables researchers to make convenient optimal transformations of multiple variables
          in datasets. This R package enables users to quickly and accurately: (1) anchor all of their 
          variables at 1.00, (2) select the desired precision with which the optimal lambda is estimated, 
          (3) apply each unique exponent to its variable, (4) rescale resultant values to within their 
          original X1 and X(n) ranges, and (5) provide original and transformed estimates of skewness, 
          kurtosis, and other inferential assessments of normality.
	"""
	
	homepage = "https://github.com/kcha193/normalr"
	cran = "normalr" 

	version("1.0.0", md5="fc641ea041e5b833249a736b5366e162")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
