# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCustomizedtraining(RPackage):
	"""Customized Training for Lasso and Elastic-Net Regularized
Generalized Linear Models

	Customized training is a simple technique for transductive
    learning, when the test covariates are known at the time of training. The
    method identifies a subset of the training set to serve as the training set
    for each of a few identified subsets in the training set. This package
    implements customized training for the glmnet() and cv.glmnet() functions.
	"""
	
	cran = "customizedTraining" 

	version("1.2", md5="1a6f93e5f730e850ad1f14d72b1473f3")

	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
