# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLassogee(RPackage):
	"""High-Dimensional Lasso Generalized Estimating Equations

	Fits generalized estimating equations with L1 regularization to longitudinal data with high dimensional covariates. Use a efficient iterative composite gradient descent algorithm.
	"""
	
	homepage = "<https://github.com/liygCR/LassoGEE>"
	cran = "LassoGEE" 

	version("1.0", md5="00b8f2b2e6dfd6f0e7f652a1df86c2f6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pgee", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-simcormultres", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
