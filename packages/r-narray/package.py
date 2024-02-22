# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNarray(RPackage):
	"""Subset- And Name-Aware Array Utility Functions

	Stacking arrays according to dimension names, subset-aware
    splitting and mapping of functions, intersecting along arbitrary
    dimensions, converting to and from data.frames, and many other helper
    functions.
	"""
	
	homepage = "https://github.com/mschubert/narray"
	cran = "narray" 

	version("0.5.1", md5="177783dcdb818aee3bc5dfad92646fbd")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
