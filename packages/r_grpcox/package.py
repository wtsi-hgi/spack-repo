# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrpcox(RPackage):
	"""Penalized Cox Model for High-Dimensional Data with Grouped
Predictors

	Fit the penalized Cox models with both non-overlapping and overlapping grouped penalties including the group lasso, group smoothly clipped absolute deviation, and group minimax concave penalty. The algorithms combine the MM approach and group-wise descent with some computational tricks including the screening, active set, and warm-start. Different tuning regularization parameter methods are provided.
	"""
	
	cran = "grpCox" 

	version("1.0.2", md5="91e1001200e54aa6c243eb2592089cfd")

	depends_on("r-matrix@1.6.1.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
