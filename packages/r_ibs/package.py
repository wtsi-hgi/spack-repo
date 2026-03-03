# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbs(RPackage):
	"""Integral of B-Spline Functions

	Calculate B-spline basis functions with a given set of knots and order, or a B-spline function with a given set of knots and order and set of de Boor points (coefficients), or the integral of a B-spline function. 
	"""
	
	cran = "ibs" 

	version("1.4", md5="008630a822ce298321e12dc3407d0bfa")

	depends_on("r-rcpp", type=("build", "run"))
