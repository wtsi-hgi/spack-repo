# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeinfo(RPackage):
	"""Gene-Environment Interaction Analysis Incorporating Prior
Information

	Realize three approaches for Gene-Environment interaction analysis. All of them adopt Sparse Group Minimax Concave Penalty to identify important G variables and G-E interactions, and simultaneously respect the hierarchy between main G and G-E interaction effects. All the three approaches are available for Linear, Logistic, and Poisson regression. Also realize to mine and construct prior information for G variables and G-E interactions.
	"""
	
	cran = "GEInfo" 

	version("1.0", md5="aec2c465b5d82296256518fa4acb84e3")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
