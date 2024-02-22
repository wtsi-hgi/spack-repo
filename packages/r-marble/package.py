# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarble(RPackage):
	"""Robust Marginal Bayesian Variable Selection for Gene-Environment
Interactions

	Recently, multiple marginal variable selection methods have been developed and shown to be effective in Gene-Environment interactions studies. We propose a novel marginal Bayesian variable selection method for Gene-Environment interactions studies. In particular, our marginal Bayesian method is robust to data contamination and outliers in the outcome variables. With the incorporation of spike-and-slab priors, we have implemented the Gibbs sampler based on Markov Chain Monte Carlo. The core algorithms of the package have been developed in 'C++'.
	"""
	
	homepage = "https://github.com/xilustat/marble"
	cran = "marble" 

	version("0.0.2", md5="dbc0af13388df9f536defedbd4a7adb8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
