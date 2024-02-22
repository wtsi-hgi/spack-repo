# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlocktools(RPackage):
	"""Block, Assign, and Diagnose Potential Interference in Randomized
Experiments

	Blocks units into experimental blocks, with one unit per treatment condition, by creating a measure of multivariate distance between all possible pairs of units.  Maximum, minimum, or an allowable range of differences between units on one variable can be set.  Randomly assign units to treatment conditions.  Diagnose potential interference between units assigned to different treatment conditions.  Write outputs to .tex and .csv files.
	"""
	
	homepage = "https://www.ryantmoore.org/html/software.blockTools.html"
	cran = "blockTools" 

	version("0.6.4", md5="f147088f4b51e3f09708a4b65b3bc338")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
