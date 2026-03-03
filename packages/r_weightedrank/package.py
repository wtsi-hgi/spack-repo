# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightedrank(RPackage):
	"""Sensitivity Analysis Using Weighted Rank Statistics

	Performs a sensitivity analysis using weighted rank tests in observational studies with I blocks of size J; see Rosenbaum (2018) <doi:10.1214/18-AOAS1153>.  The package can perform adaptive inference in block designs; see Rosenbaum (2012) <doi:10.1093/biomet/ass032>.  The main functions are wgtRank() and wgtRanktt() and ef2C().
	"""
	
	cran = "weightedRank" 

	version("0.2.5", md5="3af58b2ee47f6db07d155bc492162d98")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sensitivitymv", type=("build", "run"))
