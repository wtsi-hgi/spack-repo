# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBfsl(RPackage):
	"""Best-Fit Straight Line

	How to fit a straight line through a set of points with errors in
  both coordinates? The 'bfsl' package implements the York regression 
  (York, 2004 <doi:10.1119/1.1632486>). It provides unbiased estimates of the 
  intercept, slope and standard errors for the best-fit straight line to 
  independent points with (possibly correlated) normally distributed errors in 
  both x and y. Other commonly used errors-in-variables methods, such as 
  orthogonal distance regression, geometric mean regression or Deming regression
  are special cases of the 'bfsl' solution.
	"""
	
	homepage = "https://github.com/pasturm/bfsl"
	cran = "bfsl" 

	version("0.2.0", md5="92e5a6f05f1b55aca6d9fa05f4e743cc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
