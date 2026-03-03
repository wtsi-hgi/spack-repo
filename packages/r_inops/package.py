# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInops(RPackage):
	"""Infix Operators for Detection, Subsetting and Replacement

	Infix operators to detect, subset, and replace the elements matched by a given condition.
  The functions have several variants of operator types, including subsets, ranges, regular expressions and others.
  Implemented operators work on vectors, matrices, and lists.
	"""
	
	homepage = "https://github.com/moodymudskipper/inops"
	cran = "inops" 

	version("0.0.1", md5="43f592bdd991279d1f0f314fb3ef963e")

	depends_on("r@3.1:", type=("build", "run"))
