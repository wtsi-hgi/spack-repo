# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsemblebase(RPackage):
	"""Extensible Package for Parallel, Batch Training of Base Learners
for Ensemble Modeling

	Extensible S4 classes and methods for batch training of regression and classification algorithms such as Random Forest, Gradient Boosting Machine, Neural Network, Support Vector Machines, K-Nearest Neighbors, Penalized Regression (L1/L2), and Bayesian Additive Regression Trees. These algorithms constitute a set of 'base learners', which can subsequently be combined together to form ensemble predictions. This package provides cross-validation wrappers to allow for downstream application of ensemble integration techniques, including best-error selection. All base learner estimation objects are retained, allowing for repeated prediction calls without the need for re-training. For large problems, an option is provided to save estimation objects to disk, along with prediction methods that utilize these objects. This allows users to train and predict with large ensembles of base learners without being constrained by system RAM.
	"""
	
	cran = "EnsembleBase" 

	version("1.0.2", md5="d4741abbcaf147533e5c359ed87a86bf")

	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-bartmachine", type=("build", "run"))
