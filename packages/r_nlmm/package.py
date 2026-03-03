# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmm(RPackage):
	"""Generalized Laplace Mixed-Effects Models

	Provides functions to fit linear mixed models
	based on convolutions of the generalized Laplace (GL) distribution.
	The GL mixed-effects model includes four special cases with normal random
	effects and normal errors (NN), normal random effects and Laplace errors (NL),
	Laplace random effects and normal errors (LN), and Laplace random effects
	and Laplace errors (LL). The methods are described in Geraci and Farcomeni (2020,
	Statistical Methods in Medical Research) <doi:10.1177/0962280220903763>.
	"""
	
	cran = "nlmm" 

	version("1.1.0", md5="d9e401fcb23426418ef0a0b9afdca1a3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-lqmm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-qtools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
