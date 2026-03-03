# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCirclesintersections(RPackage):
	"""Algorithm for Computation of the Intersection Areas of N Circles

	Implementation of Librino, Levorato, and Zorzi (2014) <doi:10.1002/wcm.2305>
    algorithm for computation of the intersection areas of an arbitrary number of circles.
	"""
	
	homepage = "https://github.com/hugosal/CirclesIntersections"
	cran = "CirclesIntersections" 

	version("1.1", md5="adaf2de71d573da2c3398888c791b596")

