# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpfa(RPackage):
	"""Classification with Parallel Factor Analysis

	Classification using Richard A. Harshman's Parallel Factor Analysis-1 (Parafac) model or Parallel Factor Analysis-2 (Parafac2) model fit to a three-way or four-way data array. See Harshman and Lundy (1994): <doi:10.1016/0167-9473(94)90132-5>. Uses component weights from one mode of a Parafac or Parafac2 model as features to tune parameters for one or more classification methods via a k-fold cross-validation procedure. Allows for constraints on different tensor modes. Supports penalized logistic regression, support vector machine, random forest, feed-forward neural network, and regularized discriminant analysis. Supports binary and multiclass classification. Predicts class labels or class probabilities and calculates multiple classification performance measures. Implements parallel computing via the 'parallel' and 'doParallel' packages.
	"""
	
	cran = "cpfa" 

	version("1.1-2", md5="ba6a69923d8be4f4afc8b2c8a2c7baec")

	depends_on("r-multiway", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rda", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
