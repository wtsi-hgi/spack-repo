# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVecsets(RPackage):
	"""Like Set Tools in 'Base' Package but Keeps Duplicate Elements

	The 'base'  tools  union() intersect(), etc.,  follow the algebraic definition
 that each element of a set must be unique. 
 Since it's often helpful to compare all elements of two vectors,
 this toolset treats every element as unique for counting purposes.
 For ease of use, all functions in vecsets have an argument
 'multiple' which, when set to FALSE,
 reverts them to the base::sets (alias for all the items) tools functionality.
	"""
	
	cran = "vecsets" 

	version("1.4", md5="adb6d95043f2fe6638b53a8eccbaf0e4")

	depends_on("r-pracma", type=("build", "run"))
