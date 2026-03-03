# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTlasso(RPackage):
	"""Non-Convex Optimization and Statistical Inference for Sparse
Tensor Graphical Models

	An optimal alternating optimization algorithm for estimation of precision matrices of sparse tensor graphical models, and an efficient inference procedure for support recovery of the precision matrices.
	"""
	
	cran = "Tlasso" 

	version("1.0.2", md5="c18b028b8a5c62391ffa9a22e685c1f6")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
