# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrotter(RPackage):
	"""Pseudo-Vectors Containing All Permutations, Combinations and
Subsets of Objects Taken from a Vector

	Class definitions and constructors for pseudo-vectors containing
    all permutations, combinations and subsets of objects taken from a vector.
    Simplifies working with structures commonly encountered in combinatorics.
	"""
	
	cran = "trotter" 

	version("0.6", md5="b3d331e5400dc8330554d617b9a37db0")

