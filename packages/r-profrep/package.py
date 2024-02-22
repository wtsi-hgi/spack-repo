# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfrep(RPackage):
	"""Profile Repeatability

	Calculates profile repeatability for replicate stress response 
  curves, or similar time-series data. Profile repeatability is an individual 
  repeatability metric that uses the variances at each timepoint, the maximum 
  variance, the number of crossings (lines that cross over each other), and 
  the number of replicates to compute the repeatability score. 
  For more information see Reed et al. (2019) <doi:10.1016/j.ygcen.2018.09.015>. 
	"""
	
	homepage = "https://ubeattie.github.io/profrep/"
	cran = "profrep" 

	version("1.0.0", md5="f52f9d910c28ba1810ca9e0cb381a1e1")

	depends_on("r@2.10:", type=("build", "run"))
