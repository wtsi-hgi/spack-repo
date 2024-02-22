# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandtests(RPackage):
	"""Testing Randomness in R

	Provides several non parametric randomness tests for numeric sequences.
	"""
	
	cran = "randtests" 

	version("1.0.1", md5="a0fb51dea0ad222e57f10c703f84552c")

