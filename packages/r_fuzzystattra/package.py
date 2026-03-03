# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzystattra(RPackage):
	"""Statistical Methods for Trapezoidal Fuzzy Numbers

	The aim of the package is to provide some basic functions
 for doing statistics with trapezoidal fuzzy numbers. In particular,
  the package contains several functions for simulating trapezoidal 
  fuzzy numbers, as well as for calculating some central tendency 
  measures (mean and two types of median), some scale measures 
  (variance, ADD, MDD, Sn, Qn, Tn and some M-estimators) and 
  one diversity index and one inequality index. Moreover, 
  functions for calculating the 1-norm distance, the mid/spr 
  distance and the (phi,theta)-wabl/ldev/rdev distance between 
  fuzzy numbers are included, and a function to calculate the 
  value phi-wabl given a sample of trapezoidal fuzzy numbers.
	"""
	
	cran = "FuzzyStatTra" 

	version("1.0", md5="c8f006afed56e803d1b7755c3c531c97")

