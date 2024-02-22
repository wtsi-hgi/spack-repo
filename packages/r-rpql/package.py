# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpql(RPackage):
	"""Regularized PQL for Joint Selection in GLMMs

	Performs joint selection in Generalized Linear Mixed Models (GLMMs) using penalized likelihood methods. Specifically, the Penalized Quasi-Likelihood (PQL) is used as a loss function, and penalties are then augmented to perform simultaneous fixed and random effects selection. Regularized PQL avoids the need for integration (or approximations such as the Laplace's method) during the estimation process, and so the full solution path for model selection can be constructed relatively quickly. 
	"""
	
	cran = "rpql" 

	version("0.8.1", md5="b654a515871fac5cd89c1c1df1ed0200")

	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
