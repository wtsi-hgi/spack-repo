# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsrat(RPackage):
	"""Two-Dimensional Sociometric Status Determination with Rating
Scales

	A set of functions for two-dimensional sociometric status
    determination with rating scales. For each person assessed, SSrat computes
    probability distributions of the total scores for `Sympathy' (S),
    `Antipathy' (A), social `Preference' (P) and social `Impact' (I), and
    applies a set of criteria for sociometric status categorization.
	"""
	
	cran = "SSrat" 

	version("1.1", md5="15e612e8dcf3df528f3dddcc3b9eddf5")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
