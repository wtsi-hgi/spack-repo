# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplitfeas(RPackage):
	"""Multi-Set Split Feasibility

	An implementation of the majorization-minimization (MM) algorithm introduced by
    Xu, Chi, Yang, and Lange (2017) <arXiv:1612.05614> for solving multi-set split feasibility problems. In the multi-set split feasibility problem, we seek to find a point x
    in the intersection of multiple closed sets and whose image under a mapping also must fall in the intersection of several closed sets.
	"""
	
	cran = "splitFeas" 

	version("0.1.0", md5="86c281e37d26edeaa15dd0435f063d1f")

	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
