# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpgmm(RPackage):
	"""Bayesian Model Selection Approach for Parsimonious Gaussian
Mixture Models

	Model-based clustering using Bayesian parsimonious Gaussian mixture models.
  MCMC (Markov chain Monte Carlo) are used for parameter estimation. The RJMCMC (Reversible-jump Markov chain Monte Carlo) is used for model selection. 
  GREEN et al. (1995) <doi:10.1093/biomet/82.4.711>.
	"""
	
	cran = "bpgmm" 

	version("1.0.9", md5="d74273b6415dc965d0b9107e97ba0ccb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mcmcse@1.3.2:", type=("build", "run"))
	depends_on("r-pgmm@1.2.3:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.10:", type=("build", "run"))
	depends_on("r-mass@7.3.51.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gtools@3.8.1:", type=("build", "run"))
	depends_on("r-label-switching@1.8:", type=("build", "run"))
	depends_on("r-fabmix@5:", type=("build", "run"))
	depends_on("r-mclust@5.4.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
