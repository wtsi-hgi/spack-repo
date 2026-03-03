# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFixedpoint(RPackage):
	"""Algorithms for Finding Fixed Point Vectors of Functions

	For functions that take and return vectors (or scalars), this package provides 8 algorithms for finding fixed point vectors (vectors for which the inputs and outputs to the function are the same vector). These algorithms include Anderson (1965) acceleration <doi:10.1145/321296.321305>, epsilon extrapolation methods (Wynn 1962 <doi:10.2307/2004051>) and minimal polynomial methods (Cabay and Jackson 1976 <doi:10.1137/0713060>).
	"""
	
	cran = "FixedPoint" 

	version("0.6.3", md5="1d5127adad779d56b1d9fa56951d34e0")

	depends_on("r-mass", type=("build", "run"))
