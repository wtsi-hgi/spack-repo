# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogofgamma(RPackage):
	"""Natural Logarithms of the Gamma Function for Large Values

	Uses approximations to compute the natural logarithm of the Gamma
    function for large values.
	"""
	
	cran = "logOfGamma" 

	version("0.0.1", md5="b80d9222219087be95f98f0506437d04")

