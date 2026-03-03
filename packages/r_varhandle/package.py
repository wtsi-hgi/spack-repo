# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarhandle(RPackage):
	"""Functions for Robust Variable Handling

	Variables are the fundamental parts of each programming language but handling them efficiently might be frustrating for programmers. This package contains some functions to help user (especially data explorers) to make more sense of their variables and take the most out of variables and hardware resources. These functions are written and crafted since 2014 with years of experience in statistical data analysis on high-dimensional data, and for each of them there was a need. Functions in this package are supposed to be efficient and easy to use, hence they will be frequently updated to make them more convenient.
	"""
	
	homepage = "https://codeberg.org/mehrad/varhandle"
	cran = "varhandle" 

	version("2.0.6", md5="e124f1fcd3becf77f3ba72f66abd0cc5")

	depends_on("r@3.0.1:", type=("build", "run"))
