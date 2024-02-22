# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpamm(RPackage):
	"""Mixed-Effect Models, with or without Spatial Random Effects

	Inference based on models with or without spatially-correlated random effects, multivariate responses, or non-Gaussian random effects (e.g., Beta). Variation in residual variance (heteroscedasticity) can itself be represented by a mixed-effect model. Both classical geostatistical models (Rousset and Ferdy 2014 <doi:10.1111/ecog.00566>), and Markov random field models on irregular grids (as considered in the 'INLA' package, <https://www.r-inla.org>), can be fitted, with distinct computational procedures exploiting the sparse matrix representations for the latter case and other autoregressive models. Laplace approximations are used for likelihood or restricted  likelihood. Penalized quasi-likelihood and other variants discussed in the h-likelihood literature (Lee and Nelder 2001 <doi:10.1093/biomet/88.4.987>) are also implemented. 
	"""
	
	homepage = "https://www.r-project.org"
	cran = "spaMM" 

	version("4.4.16", md5="0e525101ec9034092e125b132e38ee5c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-gmp@0.6:", type=("build", "run"))
	depends_on("r-roi", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-geometry@0.4:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.5:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
