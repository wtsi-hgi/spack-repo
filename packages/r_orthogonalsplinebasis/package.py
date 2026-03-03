# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrthogonalsplinebasis(RPackage):
	"""Orthogonal B-Spline Basis Functions

	Represents the basis functions for B-splines in a simple matrix
    formulation that facilitates, taking integrals, derivatives, and
    making orthogonal the basis functions.
	"""
	
	homepage = "https://github.com/halpo/obsplines"
	cran = "orthogonalsplinebasis" 

	version("0.1.7", md5="7f426d631d7f28bf74fb0f531cdde0f2")

