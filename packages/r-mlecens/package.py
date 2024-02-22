# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlecens(RPackage):
	"""Computation of the MLE for Bivariate Interval Censored Data

	We provide functions to compute the nonparametric 
  maximum likelihood estimator (MLE) for 
  the bivariate distribution of (X,Y), when 
  realizations of (X,Y) cannot be observed directly. 
  To be more precise, we consider the situation 
  where we observe a set of rectangles in R^2 that are known 
  to contain the unobservable realizations of (X,Y). We
  compute the MLE based on such a set of rectangles. 
  The methods can also be used for univariate censored data (see data set
  'cosmesis'), and for 
  censored data with competing risks (see data set 'menopause'). 
  We also provide functions to visualize the observed data and the MLE. 
	"""
	
	homepage = "http://stat.ethz.ch/~maathuis/"
	cran = "MLEcens" 

	version("0.1-7", md5="f99233ccc5d5c62386bb1d4da9a63a42")

