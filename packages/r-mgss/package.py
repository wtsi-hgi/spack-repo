# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgss(RPackage):
	"""A Matrix-Free Multigrid Preconditioner for Spline Smoothing

	Data smoothing with penalized splines is a popular method and is well established for one- or two-dimensional covariates. The extension to multiple covariates is straightforward but suffers from exponentially increasing memory requirements and computational complexity. This toolbox provides a matrix-free implementation of a conjugate gradient (CG) method for the regularized least squares problem resulting from tensor product B-spline smoothing with multivariate and scattered data. It further provides matrix-free preconditioned versions of the CG-algorithm where the user can choose between a simpler diagonal preconditioner and an advanced geometric multigrid preconditioner. The main advantage is that all algorithms are performed matrix-free and therefore require only a small amount of memory. For further detail see Siebenborn & Wagner (2021).
	"""
	
	cran = "mgss" 

	version("1.2", md5="cb566971f0066577870acd95e177a704")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-combinat@0.0.8:", type=("build", "run"))
	depends_on("r-statmod@1.1:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
