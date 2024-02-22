# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRearrangement(RPackage):
	"""Monotonize Point and Interval Functional Estimates by
Rearrangement

	The rearrangement operator (Hardy,
        Littlewood, and Polya 1952) for univariate, bivariate, and
        trivariate point estimates of monotonic functions. The package
        additionally provides a function that creates simultaneous
        confidence intervals for univariate functions and applies the
        rearrangement operator to these confidence intervals.
	"""
	
	cran = "Rearrangement" 

	version("2.1", md5="09cbc82424917ad7fbe8aaaf8a2a7620")

	depends_on("r-quantreg", type=("build", "run"))
