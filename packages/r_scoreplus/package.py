# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScoreplus(RPackage):
	"""Implementation of SCORE, SCORE+ and Mixed-SCORE

	Implementation of community detection algorithm SCORE in the paper J. Jin (2015) <arXiv:1211.5803>, and SCORE+ in J. Jin, Z. Ke and S. Luo (2018) <arXiv:1811.05927>. Membership estimation algorithm called Mixed-SCORE in J. Jin, Z. Ke and S. Luo (2017) <arXiv:1708.07852>.
	"""
	
	cran = "ScorePlus" 

	version("0.1", md5="2e354ebcca14e375bd3d407a7f0b5c57")

	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-igraphdata", type=("build", "run"))
