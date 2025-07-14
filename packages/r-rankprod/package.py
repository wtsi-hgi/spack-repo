# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankprod(RPackage):
	"""Rank Product method for identifying differentially expressed genes with application in meta-analysis

	Non-parametric method for identifying differentially expressed (up- or down- regulated) genes based on the estimated percentage of false predictions (pfp). The method can combine data sets from different origins (meta-analysis) to increase the power of the identification.
	"""
	
	bioc = "RankProd"

	version("3.34.0", commit="2ff298b818661afb707947427e61b7fb41cbfc3d")
	version("3.28.0", commit="bb5556493c31600e8b861154d9fbf322eaea6190")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
