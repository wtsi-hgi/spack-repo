# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogamun(RPackage):
	"""MOGAMUN: A Multi-Objective Genetic Algorithm to Find Active Modules in Multiplex Biological Networks

	MOGAMUN is a multi-objective genetic algorithm that identifies active modules in a multiplex biological network. This allows analyzing different biological networks at the same time. MOGAMUN is based on NSGA-II (Non-Dominated Sorting Genetic Algorithm, version II), which we adapted to work on networks.
	"""
	
	homepage = "https://github.com/elvanov/MOGAMUN"
	bioc = "MOGAMUN"

	version("1.18.0", commit="fadcb6bcdb2f8e17c8fd2242f5686721b83e48fe")
	version("1.12.0", commit="4adf61f20460fe7c64356c0aa6e0061ecec4d82b")

	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
