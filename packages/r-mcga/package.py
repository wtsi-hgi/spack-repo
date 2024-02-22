# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcga(RPackage):
	"""Machine Coded Genetic Algorithms for Real-Valued Optimization
Problems

	Machine coded genetic algorithm (MCGA) is a fast tool for
    real-valued optimization problems. It uses the byte
    representation of variables rather than real-values. It
    performs the classical crossover operations (uniform) on these
    byte representations. Mutation operator is also similar to
    classical mutation operator, which is to say, it changes a
    randomly selected byte value of a chromosome by +1 or -1 with
    probability 1/2. In MCGAs there is no need for
    encoding-decoding process and the classical operators are
    directly applicable on real-values. It is fast and can handle a
    wide range of a search space with high precision. Using a
    256-unary alphabet is the main disadvantage of this algorithm
    but a moderate size population is convenient for many problems.
    Package also includes multi_mcga function for multi objective
    optimization problems. This function sorts the chromosomes
    using their ranks calculated from the non-dominated sorting
    algorithm.
	"""
	
	cran = "mcga" 

	version("3.0.7", md5="8c586bf35302c7aa777269467828ddac")

	depends_on("r-ga", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
