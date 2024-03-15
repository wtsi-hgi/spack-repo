# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolynomf(RPackage):
	"""Polynomials in R

	Implements univariate polynomial operations in R, including
  polynomial arithmetic, finding zeros, plotting, and some operations on
  lists of polynomials.
	"""
	
	cran = "PolynomF" 

	version("2.0-8", md5="88ac06ba0ec7952797e634622de5530d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
