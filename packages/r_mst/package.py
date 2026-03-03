# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMst(RPackage):
	"""Multivariate Survival Trees

	Constructs trees for multivariate survival data using marginal and frailty models.
    Grows, prunes, and selects the best-sized tree.
	"""
	
	cran = "MST" 

	version("2.2", md5="c431f475043555daa3845ced06b6016b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
