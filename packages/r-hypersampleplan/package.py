# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypersampleplan(RPackage):
	"""Attribute Sampling Plan with Exact Hypergeometric Probabilities
using Chebyshev Polynomials

	Implements an algorithm for efficient and exact calculation of hypergeometric 
    and binomial probabilities using Chebyshev polynomials, while other algorithm use an 
    approximation when N is large. A useful applications is also considered in this package 
    for the construction of attribute sampling plans which is an important field of statistical
    quality control. The quantile, and the confidence limit for the attribute sampling plan are
    also implemented in this package. The hypergeometric distribution can be represented in 
    terms of Chebyshev polynomials. This representation is particularly useful in the calculation
    of exact values of hypergeometric variables. 
	"""
	
	cran = "hypersampleplan" 

	version("0.1.1", md5="e9db2539fa55c489042afa4e59057f85")

