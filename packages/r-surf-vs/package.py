# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurfVs(RPackage):
	"""Subsampling Ranking Forward Selection (SuRF)

	Performs variable selection based on subsampling, ranking forward selection. Details of the method are published in Lihui Liu, Hong Gu, Johan Van Limbergen, Toby Kenney (2020) SuRF: A new method for sparse variable selection, with application in microbiome data analysis  Statistics in Medicine 40 897-919 <doi:10.1002/sim.8809>. Xo is the matrix of predictor variables. y is the response variable. Currently only binary responses using logistic regression are supported. X is a matrix of additional predictors which should be scaled to have sum 1 prior to analysis. fold is the number of folds for cross-validation. Alpha is the parameter for the elastic net method used in the subsampling procedure: the default value of 1 corresponds to LASSO. prop is the proportion of variables to remove in the each subsample. weights indicates whether observations should be weighted by class size. When the class sizes are unbalanced, weighting observations can improve results. B is the number of subsamples to use for ranking the variables. C is the number of permutations to use for estimating the critical value of the null distribution. If the 'doParallel' package is installed, the function can be run in parallel by setting ncores to the number of threads to use. If the default value of 1 is used, or if the 'doParallel' package is not installed, the function does not run in parallel. display.progress indicates whether the function should display messages indicating its progress. family is a family variable for the glm() fitting. Note that the 'glmnet' package does not permit the use of nonstandard link functions, so will always use the default link function. However, the glm() fitting will use the specified link. The default is binomial with logistic regression, because this is a common use case. pval is the p-value for inclusion of a variable in the model. Under the null case, the number of false positives will be geometrically distributed with this as probability of success, so if this parameter is set to p, the expected number of false positives should be p/(1-p).
	"""
	
	cran = "SuRF.vs" 

	version("1.1.0.1", md5="584f0aa68a8496b7c5440a5762b76cc7")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
