# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdspls(RPackage):
	"""Data-Driven Sparse Partial Least Squares

	A sparse Partial Least Squares implementation which uses soft-threshold
	estimation of the covariance matrices and therein introduces
	sparsity. Number of components and regularization coefficients are automatically set.
	"""
	
	cran = "ddsPLS" 

	version("1.2.1", md5="5d48f0611a975e9146073d8abe538c28")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
