# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLenght(RPackage):
	"""Allow Misspellings of Length Function

	Convenient aliases for common ways of misspelling the base R function length(). These include every permutation of the final three letters.
	"""
	
	cran = "lenght" 

	version("0.1.0", md5="0e7c98e93699640ec8d44de1d1d50ff8")

