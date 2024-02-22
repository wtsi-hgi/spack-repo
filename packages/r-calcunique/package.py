# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalcunique(RPackage):
	"""Simple Wrapper for Computationally Expensive Functions

	This is a one-function package that will pass only unique values to a computationally-expensive function that returns an output of the same length as the input.
    In importing and working with tidy data, it is common to have index columns, often including time stamps that are far from unique. Some functions to work with these such as text conversion to other variable types (e.g. as.POSIXct()), various grep()-based functions, and often the cut() function are relatively slow when working with tens of millions of rows or more.
	"""
	
	homepage = "https://github.com/stephenbfroehlich/calcUnique"
	cran = "calcUnique" 

	version("0.1.2", md5="bb94b26cfba208c0a9bc6dc4c887606f")

