# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWlogit(RPackage):
	"""Variable Selection in High-Dimensional Logistic Regression
Models using a Whitening Approach

	It proposes a novel variable selection approach in classification problem that takes into account the correlations that may exist between the predictors of the design matrix in a high-dimensional logistic model. Our approach consists in rewriting the initial high-dimensional logistic model to remove the correlation between the predictors and in applying the generalized Lasso criterion.
	"""
	
	cran = "WLogit" 

	version("2.1", md5="4587388c3cb61378c6007f8f4c22a936")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cvcovest", type=("build", "run"))
	depends_on("r-genlasso", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
