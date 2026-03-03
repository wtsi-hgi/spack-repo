# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcodist(RPackage):
	"""Dissimilarity-Based Functions for Ecological Analysis

	Dissimilarity-based analysis functions including ordination and Mantel test functions, intended for use with spatial and community ecological data. The original package description is in Goslee and Urban (2007) <doi:10.18637/jss.v022.i07>, with further statistical detail in Goslee (2010) <doi:10.1007/s11258-009-9641-0>.
	"""
	
	cran = "ecodist" 

	version("2.1.3", md5="058ddf74210376f4e1e7af2a5e2bb2a2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
