# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlexperiments(RPackage):
	"""Machine Learning Experiments

	Provides 'R6' objects to perform parallelized hyperparameter
    optimization and cross-validation. Hyperparameter optimization can be
    performed with Bayesian optimization (via 'ParBayesianOptimization'
    <https://cran.r-project.org/package=ParBayesianOptimization>) and grid
    search. The optimized hyperparameters can be validated using k-fold
    cross-validation. Alternatively, hyperparameter optimization and
    validation can be performed with nested cross-validation. While
    'mlexperiments' focuses on core wrappers for machine learning
    experiments, additional learner algorithms can be supplemented by
    inheriting from the provided learner base class.
	"""
	
	homepage = "https://github.com/kapsner/mlexperiments"
	cran = "mlexperiments" 

	version("0.0.2", md5="be46f42efdd4fa77ef303cbea5165c20")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-kdry", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-splittools", type=("build", "run"))
