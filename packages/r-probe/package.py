# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbe(RPackage):
	"""Sparse High-Dimensional Linear Regression with PROBE

	Implements an efficient and powerful Bayesian approach for sparse high-dimensional linear regression. It uses minimal prior assumptions on the parameters through plug-in empirical Bayes estimates of hyperparameters. An efficient Parameter-Expanded Expectation-Conditional-Maximization (PX-ECM) algorithm estimates maximum a posteriori (MAP) values of regression parameters and variable selection probabilities. The PX-ECM results in a robust computationally efficient coordinate-wise optimization, which adjusts for the impact of other predictor variables. The E-step is motivated by the popular two-group approach to multiple testing. The result is a PaRtitiOned empirical Bayes Ecm (PROBE) algorithm applied to sparse high-dimensional linear regression, implemented using one-at-a-time or all-at-once type optimization. More information can be found in McLain, Zgodic, and Bondell (2022) <arXiv:2209.08139>.
	"""
	
	cran = "probe" 

	version("1.1", md5="aa491058e5a0589ba180a97aa62530c0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
