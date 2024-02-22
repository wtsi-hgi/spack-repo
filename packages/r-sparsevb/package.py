# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsevb(RPackage):
	"""Spike-and-Slab Variational Bayes for Linear and Logistic
Regression

	Implements variational Bayesian algorithms to perform scalable variable selection for sparse, high-dimensional linear and logistic regression models. Features include a novel prioritized updating scheme, which uses a preliminary estimator of the variational means during initialization to generate an updating order prioritizing large, more relevant, coefficients. Sparsity is induced via spike-and-slab priors with either Laplace or Gaussian slabs. By default, the heavier-tailed Laplace density is used. Formal derivations of the algorithms and asymptotic consistency results may be found in Kolyan Ray and Botond Szabo (2020) <doi:10.1080/01621459.2020.1847121> and Kolyan Ray, Botond Szabo, and Gabriel Clara (2020) <arXiv:2010.11665>.
	"""
	
	cran = "sparsevb" 

	version("0.1.0", md5="fb0aeb286486d47739d91126df2b3a86")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-selectiveinference@1.2.5:", type=("build", "run"))
	depends_on("r-glmnet@4.0.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppensmallen", type=("build", "run"))
