# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REztune(RPackage):
	"""Tunes AdaBoost, Elastic Net, Support Vector Machines, and
Gradient Boosting Machines

	Contains two functions that are intended to make
    tuning supervised learning methods easy. The eztune function uses a
    genetic algorithm or Hooke-Jeeves optimizer to find the best 
    set of tuning parameters. The user can choose the optimizer, the 
    learning method, and if optimization will be based on accuracy 
    obtained through validation error, cross validation, or resubstitution. 
    The function eztune.cv will compute a cross validated error rate. The purpose 
    of eztune_cv is to provide a cross validated accuracy or MSE when 
    resubstitution or validation data are used for optimization because 
    error measures from both approaches can be misleading.
	"""
	
	cran = "EZtune" 

	version("3.1.1", md5="53c7837a42f53ac7def3dd6eb750d5e3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ada", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
