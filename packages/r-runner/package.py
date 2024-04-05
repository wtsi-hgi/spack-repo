# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRunner(RPackage):
	"""Running Operations for Vectors

	Lightweight library for rolling windows operations. Package enables
  full control over the window length, window lag and a time indices. With a runner 
  one can apply any R function on a rolling windows. The package eases work with 
  equally and unequally spaced time series.
	"""
	
	cran = "runner" 

	version("0.4.4", md5="95548e412fa9363125fb6eaaffe4d3db")
	version("0.4.3", md5="4330e09c5a3553311f5437e3bdeaf78c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
