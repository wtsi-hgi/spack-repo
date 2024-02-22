# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayenet(RPackage):
	"""Bayesian Quantile Elastic Net for Genetic Study

	As heavy-tailed error distribution and outliers in the response variable widely exist, models which are robust to data contamination are highly demanded. Here, we develop a novel robust Bayesian variable selection method with elastic net penalty for quantile regression in genetic analysis. In particular, the spike-and-slab priors have been incorporated to impose sparsity. An efficient Gibbs sampler has been developed to facilitate computation.The core modules of the package have been developed in 'C++' and R.
	"""
	
	cran = "Bayenet" 

	version("0.1", md5="e269ad01b3a059ac85609b4202d95a38")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-hbmem", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
