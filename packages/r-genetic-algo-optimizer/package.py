# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneticAlgoOptimizer(RPackage):
	"""Genetic Algorithm Optimization

	Genetic algorithm are a class of optimization
    algorithms inspired by the process of natural selection and genetics.
    This package is for learning purposes and allows users to optimize
    various functions or parameters by mimicking biological evolution
    processes such as selection, crossover, and mutation. Ideal for tasks
    like machine learning parameter tuning, mathematical function
    optimization, and solving combinatorial problems.
	"""
	
	homepage = "https://danymukesha.github.io/genetic.algo.optimizeR/"
	cran = "genetic.algo.optimizeR" 

	version("0.2.6", md5="0109b8a8dee1e4f4f969f74eca340fa2")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rsconnect", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tinytex", type=("build", "run"))
	depends_on("r-biocviews", type=("build", "run"))
