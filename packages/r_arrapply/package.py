# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrapply(RPackage):
	"""Apply a Function to a Margin of an Array

	High performance variant of apply() for a fixed set of functions.
  Considerable speedup of this implementation is a trade-off for universality: user defined
  functions cannot be used with this package. However, about 20 most currently employed
  functions are available for usage. They can be divided in three types:
  reducing functions (like mean(), sum() etc., giving a scalar when applied to a vector),
  mapping function (like normalise(), cumsum() etc., giving a vector of the same length
  as the input vector) and finally, vector reducing function (like diff() which produces
  result vector of a length different from the length of input vector).
  Optional or mandatory additional arguments required by some functions
  (e.g. norm type for norm()) can be
  passed as named arguments in '...'.
	"""
	
	cran = "arrApply" 

	version("2.2", md5="c6feda67c5a781e635dd221c4eaeb50e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
