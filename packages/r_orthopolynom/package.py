# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrthopolynom(RPackage):
	"""Collection of Functions for Orthogonal and Orthonormal
Polynomials

	A collection of functions to construct sets of orthogonal
        polynomials and their recurrence relations. Additional
        functions are provided to calculate the derivative, integral,
        value and roots of lists of polynomial objects.
	"""
	
	cran = "orthopolynom" 

	version("1.0-6.1", md5="043f7ec6fccafc90b2133c7f7f84c048")

	depends_on("r@2.0.1:", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
