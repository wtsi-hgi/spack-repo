# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsev(RPackage):
	"""Sample Size Computation for Fixed N with Optimal Reward

	Computes the optimal sample size for various 2-group designs (e.g., when comparing the means of two groups assuming equal variances, unequal variances, or comparing proportions) when the aim is to maximize the rewards over the full decision procedure of a) running a trial (with the computed sample size), and b) subsequently administering the winning treatment to the remaining N-n units in the population. Sample sizes and expected rewards for standard t- and z- tests are also provided.
	"""
	
	cran = "ssev" 

	version("0.1.0", md5="46335b77554827bb4913b63ee23cd21f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
	depends_on("r-mess", type=("build", "run"))
