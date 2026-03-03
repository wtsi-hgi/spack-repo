# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdana(RPackage):
	"""Adaptive Nature-Inspired Algorithms for Hybrid Genetic
Optimization

	The Genetic Algorithm (GA) is a type of optimization method of Evolutionary Algorithms. It uses the biologically inspired operators such as mutation, crossover, selection and replacement.Because of their global search and robustness abilities, GAs have been widely utilized in machine learning, expert systems, data science, engineering, life sciences and many other areas of research and business. However, the regular GAs need the techniques to improve their efficiency in computing time and performance in finding global optimum using some adaptation and hybridization strategies. The adaptive GAs (AGA) increase the convergence speed and success of regular GAs by setting the parameters crossover and mutation probabilities dynamically. The hybrid GAs combine the exploration strength of a stochastic GAs with the exact convergence ability of any type of deterministic local search algorithms such as simulated-annealing, in addition to other nature-inspired algorithms such as ant colony optimization, particle swarm optimization etc. The package 'adana' includes a rich working environment with its many functions that make possible to build and work regular GA, adaptive GA, hybrid GA and hybrid adaptive GA for any kind of optimization problems. Cebeci, Z. (2021, ISBN: 9786254397448).
	"""
	
	cran = "adana" 

	version("1.1.0", md5="cbbc8e42940ea9ad140368b316f59980")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-roi", type=("build", "run"))
	depends_on("r-roi-plugin-optimx", type=("build", "run"))
