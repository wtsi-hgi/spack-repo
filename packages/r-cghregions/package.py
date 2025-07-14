# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCghregions(RPackage):
	"""Dimension Reduction for Array CGH Data with Minimal Information Loss.

	Dimension Reduction for Array CGH Data with Minimal Information Loss
	"""
	
	bioc = "CGHregions"

	version("1.66.0", commit="952b8215f7ca2ff9898415760ebb3c57e32d7d5d")
	version("1.60.0", commit="bab0f30b4dc57d70a30be3c39cd82badb880fff4")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-cghbase", type=("build", "run"))
