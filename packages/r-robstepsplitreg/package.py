# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobstepsplitreg(RPackage):
	"""Robust Stepwise Split Regularized Regression

	Functions to perform robust stepwise split regularized regression. The approach first 
             uses a robust stepwise algorithm to split the variables into the models of an ensemble. 
             An adaptive robust regularized estimator is then applied to each subset of predictors
             in the models of an ensemble. 
	"""
	
	cran = "robStepSplitReg" 

	version("1.1.0", md5="b0ed45aa7b7231f214bb1713e1060843")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cellwise", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
