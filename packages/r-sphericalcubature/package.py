# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSphericalcubature(RPackage):
	"""Numerical Integration over Spheres and Balls in n-Dimensions;
Multivariate Polar Coordinates

	Provides several methods to integrate functions over the unit
 sphere and ball in n-dimensional Euclidean space.  Routines for converting to/from
 multivariate polar/spherical coordinates are also provided.
	"""
	
	cran = "SphericalCubature" 

	version("1.5", md5="f6b5e10165400ed46fb865a7c102daf7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-simplicialcubature@1.3:", type=("build", "run"))
	depends_on("r-mvmesh", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
