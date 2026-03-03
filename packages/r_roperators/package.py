# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoperators(RPackage):
	"""Additional Operators to Help you Write Cleaner R Code

	Provides string arithmetic, reassignment operators, logical operators
  that handle missing values, and extra logical operators such as floating point
  equality and all or nothing. The intent is to allow R users to write code that
  is easier to read, write, and maintain while providing a friendlier experience
  to new R users from other language backgrounds (such as 'Python') who are used
  to concepts such as x += 1 and 'foo' + 'bar'.
  Includes operators for not in, easy floating point comparisons, === equivalent, and SQL-like 
  like operations (), etc. 
  We also added in some extra helper functions, such as OS checks, pasting
  in Oxford comma format, and functions to get the first, last, nth, or most common 
  element of a vector or word in a string. 
	"""
	
	homepage = "https://benwiseman.github.io/roperators/"
	cran = "roperators" 

	version("1.3.14", md5="db0fc6cf5a4073ae7b531392e0376c44")

	depends_on("r@3:", type=("build", "run"))
