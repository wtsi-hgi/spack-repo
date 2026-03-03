# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpmerge(RPackage):
	"""Merging Linkage Maps by Linear Programming

	Creates a consensus genetic map by merging linkage maps from different populations.  The software uses linear programming (LP) to efficiently minimize the mean absolute error between the consensus map and the linkage maps.  This minimization is performed subject to linear inequality constraints that ensure the ordering of the markers in the linkage maps is preserved.  When marker order is inconsistent between linkage maps, a minimum set of ordinal constraints is deleted to resolve the conflicts.
	"""
	
	homepage = "http://potatobreeding.cals.wisc.edu/software"
	cran = "LPmerge" 

	version("1.7", md5="17289e3a533afcac4002a5ff972396b1")

	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
