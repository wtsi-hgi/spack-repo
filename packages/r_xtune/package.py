# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXtune(RPackage):
	"""Regularized Regression with Feature-Specific Penalties
Integrating External Information

	Extends standard penalized regression (Lasso, Ridge, and Elastic-net) to allow feature-specific shrinkage based on external information with the goal of achieving a better prediction accuracy and variable selection. Examples of external information include the grouping of predictors, prior knowledge of biological importance, external p-values, function annotations, etc. The choice of multiple tuning parameters is done using an Empirical Bayes approach. A majorization-minimization algorithm is employed for implementation. 
	"""
	
	homepage = "https://github.com/JingxuanH/xtune"
	cran = "xtune" 

	version("2.0.0", md5="6cc47a49f24c22bca1ab9a1a09f07a27")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-selectiveinference", type=("build", "run"))
	depends_on("r-lbfgs", type=("build", "run"))
