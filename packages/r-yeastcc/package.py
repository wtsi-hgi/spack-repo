# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastcc(RPackage):
	"""Spellman et al. (1998) and Pramila/Breeden (2006) yeast cell cycle microarray data

	ExpressionSet for Spellman et al. (1998) yeast cell cycle microarray experiment
	"""
	
	bioc = "yeastCC"

	version("1.48.0", commit="8708bd9a8312dbe7b79245767d13d10336ae9df7")
	version("1.42.0", commit="86d942035bea77f2b3a195c0732035e0af4f4dd3")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))

