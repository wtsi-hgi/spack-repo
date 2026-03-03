# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3tuning(RPackage):
	"""Hyperparameter Optimization for 'mlr3'

	Hyperparameter optimization package of the 'mlr3' ecosystem. It
    features highly configurable search spaces via the 'paradox' package and
    finds optimal hyperparameter configurations for any 'mlr3' learner.
    'mlr3tuning' works with several optimization algorithms e.g. Random
    Search, Iterated Racing, Bayesian Optimization (in 'mlr3mbo') and
    Hyperband (in 'mlr3hyperband'). Moreover, it can automatically optimize
    learners and estimate the performance of optimized models with nested
    resampling.
	"""
	
	homepage = "https://mlr3tuning.mlr-org.com"
	cran = "mlr3tuning" 

	version("0.20.0", md5="5982779679aef64eeb4c4df15862a73e")
	version("0.19.2", md5="6131c966786a64a1e66907519784dfb3")

	depends_on("r-mlr3@0.17:", type=("build", "run"))
	depends_on("r-paradox@0.10:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-bbotk@0.7.3:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-mlr3misc@0.13:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
