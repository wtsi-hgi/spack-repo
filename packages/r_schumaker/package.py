# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchumaker(RPackage):
	"""Schumaker Shape-Preserving Spline

	This is a shape preserving spline <doi:10.1137/0720057>
    which is guaranteed to be monotonic and concave or convex if the
    data is monotonic and concave or convex. It does not use any 
    optimisation and is therefore quick and smoothly converges to a 
    fixed point in economic dynamics problems including value function 
    iteration. It also automatically gives the first two derivatives 
    of the spline and options for determining behaviour when evaluated 
    outside the interpolation domain.
	"""
	
	cran = "schumaker" 

	version("1.2.1", md5="0895ffd1707ec8ec71a8d7b7d65fe0c7")

