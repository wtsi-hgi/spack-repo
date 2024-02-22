# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFractional(RPackage):
	"""Vulgar Fractions in R

	The main function of this package allows numerical vector objects to
  be displayed with their values in vulgar fractional form.  This is convenient if
  patterns can then be more easily detected.  In some cases replacing the components
  of a numeric vector by a rational approximation can also be expected to remove
  some component of round-off error.  The main functions form a re-implementation
  of the functions 'fractions' and 'rational' of the MASS package, but using a
  radically improved programming strategy.
	"""
	
	cran = "fractional" 

	version("0.1.3", md5="e33165a29333e4a8ac11b3e9db006907")

	depends_on("r-rcpp", type=("build", "run"))
