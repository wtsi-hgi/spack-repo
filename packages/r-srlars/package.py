# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrlars(RPackage):
	"""Split Robust Least Angle Regression

	Functions to perform split robust least angle regression. The approach first uses the
             least angle regression algorithm to split the variables into the models of an ensemble
             and robust estimates of the correlation between predictors. An elastic net estimator is 
             then applied to the selected predictors in each model using the imputed data from the
             detect deviating cell (DDC) method.
	"""
	
	cran = "srlars" 

	version("1.0.1", md5="f39da95e82a01553c24d7f768c3b75a0")

	depends_on("r-cellwise", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
