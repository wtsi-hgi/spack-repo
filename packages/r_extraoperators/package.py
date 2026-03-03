# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtraoperators(RPackage):
	"""Extra Binary Relational and Logical Operators

	Speed up common tasks, particularly logical or
  relational comparisons and routine follow up tasks such as finding the
  indices and subsetting. Inspired by mathematics, where something like:
  3 < x < 6 is a standard, elegant and clear way to assert that
  x is both greater than 3 and less than 6
  (see for example <https://en.wikipedia.org/wiki/Relational_operator>),
  a chaining operator is implemented. The chaining operator, %c%,
  allows multiple relational operations to be used in quotes on the right
  hand side for the same object, on the left hand side.
  The %e% operator allows something like set-builder notation 
  (see for example <https://en.wikipedia.org/wiki/Set-builder_notation>) 
  to be used on the right hand side.
  All operators have built in prefixes defined for all, subset, and which
  to reduce the amount of code needed for common tasks, such as return those
  values that are true.
	"""
	
	homepage = "https://joshuawiley.com/extraoperators/"
	cran = "extraoperators" 

	version("0.3.0", md5="3aee976d939552e48f9de8c02180044b")

