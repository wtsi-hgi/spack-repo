# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplicialcubature(RPackage):
	"""Integration of Functions Over Simplices

	Provides methods to integrate functions over m-dimensional simplices
 in n-dimensional Euclidean space.  There are exact methods for polynomials and
 adaptive methods for integrating an arbitrary function.  
	"""
	
	cran = "SimplicialCubature" 

	version("1.3", md5="cf777c9ac4b997960e7cbf8a532cf9d4")

	depends_on("r@3:", type=("build", "run"))
