# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPursuit(RPackage):
	"""Projection Pursuit

	Projection pursuit (PP) with 17 methods and grand tour with 3 methods. Being that projection pursuit searches for low-dimensional linear projections in high-dimensional data structures, while grand tour is a technique used to explore multivariate statistical data through animation.
	"""
	
	cran = "Pursuit" 

	version("1.0.4", md5="27b6985dd0e5aed62ac5adcc4920de26")

	depends_on("r-mass", type=("build", "run"))
