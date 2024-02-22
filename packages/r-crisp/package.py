# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisp(RPackage):
	"""Fits a Model that Partitions the Covariate Space into Blocks in
a Data- Adaptive Way

	Implements convex regression with interpretable sharp partitions
    (CRISP), which considers the problem of predicting an outcome variable on the basis of two covariates, using an interpretable yet non-additive model. CRISP partitions the covariate space into blocks in a data-adaptive way, and fits a mean model within each block. Unlike other partitioning methods, CRISP is fit using a non-greedy approach by solving a convex optimization problem, resulting in low-variance fits. More details are provided in Petersen, A., Simon, N., and Witten, D. (2016). Convex Regression with Interpretable Sharp Partitions. Journal of Machine Learning Research, 17(94): 1-31 <http://jmlr.org/papers/volume17/15-344/15-344.pdf>.
	"""
	
	cran = "crisp" 

	version("1.0.0", md5="99920612d052eeea3e04932c322e8782")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
