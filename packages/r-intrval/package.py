# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntrval(RPackage):
	"""Relational Operators for Intervals

	Evaluating if values
  of vectors are within different open/closed intervals
  (`x %[]% c(a, b)`), or if two closed
  intervals overlap (`c(a1, b1) %[]o[]% c(a2, b2)`).
  Operators for negation and directional relations also implemented.
	"""
	
	homepage = "https://github.com/psolymos/intrval"
	cran = "intrval" 

	version("0.1-2", md5="a176656aadcba2b9daf3da0b1bfdf123")

