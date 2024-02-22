# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratbr(RPackage):
	"""Optimal Stratification in Stratified Sampling

	An Optimization Algorithm Applied to
    Stratification Problem.This function aims
    at constructing optimal strata with an optimization algorithm
    based on a global optimisation technique called Biased
    Random Key Genetic Algorithms.
	"""
	
	cran = "stratbr" 

	version("1.2", md5="09816e29ec4cfb3ab8400e01415c64a8")

	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-stratification", type=("build", "run"))
