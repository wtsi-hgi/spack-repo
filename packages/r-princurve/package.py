# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrincurve(RPackage):
	"""Fit a Principal Curve in Arbitrary Dimension

	Fitting a principal curve to a data matrix in arbitrary dimensions. 
  Hastie and Stuetzle (1989) <doi:10.2307/2289936>.
	"""
	
	homepage = "https://github.com/rcannood/princurve"
	cran = "princurve" 

	version("2.1.6", md5="770b85636866f3a1948f0bb724436f2b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
