# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlare(RPackage):
	"""Family of Lasso Regression

	Provide the implementation of a family of Lasso variants including Dantzig Selector, LAD Lasso, SQRT Lasso, Lq Lasso for estimating high dimensional sparse linear model. We adopt the alternating direction method of multipliers and convert the original optimization problem into a sequential L1 penalized least square minimization problem, which can be efficiently solved by linearization algorithm. A multi-stage screening approach is adopted for further acceleration. Besides the sparse linear model estimation, we also provide the extension of these Lasso variants to sparse Gaussian graphical model estimation including TIGER and CLIME using either L1 or adaptive penalty. Missing values can be tolerated for Dantzig selector and CLIME. The computation is memory-optimized using the sparse matrix output. For more information, please refer to <https://www.jmlr.org/papers/volume16/li15a/li15a.pdf>.
	"""
	
	cran = "flare" 

	version("1.7.0.1", md5="64b0b54c67bd9924a9c8e1a6159682df")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
