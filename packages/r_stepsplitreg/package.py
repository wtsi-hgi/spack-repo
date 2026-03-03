# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepsplitreg(RPackage):
	"""Stepwise Split Regularized Regression

	Functions to perform stepwise split regularized regression. The approach first 
             uses a stepwise algorithm to split the variables into the models with a goodness
             of fit criterion, and then regularization is applied to each model. The weights 
             of the models in the ensemble are determined based on a criterion selected by 
             the user.
	"""
	
	cran = "stepSplitReg" 

	version("1.0.3", md5="e7f2f9df5e892d6effaee86278f499f7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-splitglm", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
