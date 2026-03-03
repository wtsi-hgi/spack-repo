# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImmigrate(RPackage):
	"""Iterative Max-Min Entropy Margin-Maximization with Interaction
Terms for Feature Selection

	Based on large margin principle, this package performs feature selection methods: "IM4E"(Iterative Margin-Maximization under Max-Min Entropy Algorithm); "Immigrate"(Iterative Max-Min Entropy Margin-Maximization with Interaction Terms Algorithm); "BIM"(Boosted version of IMMIGRATE algorithm); "Simba"(Iterative Search Margin Based Algorithm); "LFE"(Local Feature Extraction Algorithm). This package also performs prediction for the above feature selection methods.
	"""
	
	homepage = "https://cran.r-project.org/package=Immigrate"
	cran = "Immigrate" 

	version("0.2.1", md5="3ca45d209bee6dfb8b86eea7fe65cf87")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
