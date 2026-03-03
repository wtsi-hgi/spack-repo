# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJocre(RPackage):
	"""Joint Confidence Regions

	Computing and plotting joint confidence regions and intervals. Regions include classical ellipsoids, minimum-volume or minimum-length regions, and an empirical Bayes region. Intervals include the TOST procedure with ordinary or expanded intervals and a fixed-sequence procedure. Such regions and intervals are useful e.g., for the assessment of multi-parameter (bio-)equivalence. Joint confidence regions for the mean and variance of a normal distribution are available as well.
	"""
	
	cran = "jocre" 

	version("0.3.3", md5="dbf9d1b9a353587b8ceddcbb6c2e72c8")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
