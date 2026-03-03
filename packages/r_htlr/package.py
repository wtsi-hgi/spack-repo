# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtlr(RPackage):
	"""Bayesian Logistic Regression with Heavy-Tailed Priors

	Efficient Bayesian multinomial logistic regression based on heavy-tailed
  (hyper-LASSO, non-convex) priors. The posterior of coefficients and hyper-parameters
  is sampled with restricted Gibbs sampling for leveraging the high-dimensionality and
  Hamiltonian Monte Carlo for handling the high-correlation among coefficients. A detailed
  description of the method: Li and Yao (2018), 
  Journal of Statistical Computation and Simulation, 88:14, 2827-2851, <arXiv:1405.3319>.
	"""
	
	homepage = "https://longhaisk.github.io/HTLR/"
	cran = "HTLR" 

	version("0.4-4", md5="933240b19eab55877eae808728b0325e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-bcbcsf", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
