# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermanova(RPackage):
	"""Multivariate Analysis of Variance Based on Distances and
Permutations

	Calculates multivariate analysis of variance based on permutations and some associated pictorial representations. The pictorial representation is based on the principal coordinates of the group means. There are some original results that will be published soon. 
	"""
	
	cran = "PERMANOVA" 

	version("0.2.0", md5="1b730626585c982689edad14d01f9933")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
