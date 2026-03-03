# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParbayesianoptimization(RPackage):
	"""Parallel Bayesian Optimization of Hyperparameters

	Fast, flexible framework for implementing Bayesian optimization of model 
	hyperparameters according to the methods described in Snoek et al. <arXiv:1206.2944>.
	The package allows the user to run scoring function in parallel, save intermediary 
	results, and tweak other aspects of the process to fully utilize the computing resources
	available to the user.
	"""
	
	homepage = "https://github.com/AnotherSamWilson/ParBayesianOptimization"
	cran = "ParBayesianOptimization" 

	version("1.2.6", md5="24dd3cf1e6f3d8b6c004ee610f4f26de")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr@0.2.4:", type=("build", "run"))
