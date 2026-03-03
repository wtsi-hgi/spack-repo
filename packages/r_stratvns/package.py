# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratvns(RPackage):
	"""Optimal Stratification in Stratified Sampling

	An Optimization Algorithm Applied to
    Stratification Problem.This function aims
    at constructing optimal strata with an optimization algorithm
    based on a global optimisation technique called vns.
	"""
	
	cran = "stratvns" 

	version("1.1", md5="35efb3c3cf965f95f18990df4e778b7c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-multalloc", type=("build", "run"))
