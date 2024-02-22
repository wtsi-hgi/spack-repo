# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemodelr(RPackage):
	"""Simulating Differential Equations with Data

	Designed to support the visualization, numerical computation,
     qualitative analysis, model-data fusion, and stochastic simulation for
     autonomous systems of differential equations. Euler and Runge-Kutta methods
     are implemented, along with tools to visualize the two-dimensional
     phaseplane. Likelihood surfaces and a simple Markov Chain Monte Carlo
     parameter estimator can be used for model-data fusion of differential
     equations and empirical models. The Euler-Maruyama method is provided for
     simulation of stochastic differential equations. The package was originally
     written for internal use to support teaching by Zobitz, and refined to
     support the text "Exploring modeling with data and differential equations
     using R" by John Zobitz (2021) <https://jmzobitz.github.io/ModelingWithR/index.html>.
	"""
	
	cran = "demodelr" 

	version("1.0.1", md5="ec02ab73d686f3393a5ed3f4816fa0b6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
