# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDidacticboost(RPackage):
	"""A Simple Implementation and Demonstration of Gradient Boosting

	A basic, clear implementation of tree-based gradient boosting
    designed to illustrate the core operation of boosting models. Tuning
    parameters (such as stochastic subsampling, modified learning rate, or
    regularization) are not implemented. The only adjustable parameter is the
    number of training rounds. If you are looking for a high performance boosting
    implementation with tuning parameters, consider the 'xgboost' package.
	"""
	
	homepage = "https://github.com/dashaub/DidacticBoost"
	cran = "DidacticBoost" 

	version("0.1.1", md5="619919f52472615e4ff74b1a1811ad46")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rpart@4.1.10:", type=("build", "run"))
