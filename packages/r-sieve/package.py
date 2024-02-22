# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSieve(RPackage):
	"""Nonparametric Estimation by the Method of Sieves

	Performs multivariate nonparametric regression/classification by the method of sieves (using orthogonal basis). The method is suitable for moderate high-dimensional features (dimension < 100). The l1-penalized sieve estimator, a nonparametric generalization of Lasso, is adaptive to the feature dimension with provable theoretical guarantees. We also include a nonparametric stochastic gradient descent estimator, Sieve-SGD, for online or large scale batch problems. Details of the methods can be found in: <arXiv:2206.02994> <arXiv:2104.00846><arXiv:2310.12140>.
	"""
	
	cran = "Sieve" 

	version("2.1", md5="6ce13900cddfb2794ff8c4d1c6c7a3ec")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
