# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyr(RPackage):
	"""Model Based Phylogenetic Analysis

	A collection of functions to do model-based phylogenetic analysis. 
    It includes functions to calculate community phylogenetic diversity,
    to estimate correlations among functional traits while accounting for 
    phylogenetic relationships, and to fit phylogenetic generalized linear
    mixed models. The Bayesian phylogenetic generalized linear mixed models
    are fitted with the 'INLA' package (<https://www.r-inla.org>).
	"""
	
	homepage = "https://daijiang.github.io/phyr/"
	cran = "phyr" 

	version("1.1.0", md5="097bfb4197ffbe1adce359fde3e3ba16")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
