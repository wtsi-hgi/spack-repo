# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGena(RPackage):
	"""Genetic Algorithm and Particle Swarm Optimization

	Implements genetic algorithm and particle swarm algorithm for real-valued functions. Various modifications (including hybridization and elitism) of these algorithms are provided. Implemented functions are based on ideas described in S. Katoch, S. Chauhan, V. Kumar (2020) <doi:10.1007/s11042-020-10139-6> and M. Clerc (2012) <https://hal.archives-ouvertes.fr/hal-00764996>.
	"""
	
	cran = "gena" 

	version("1.0.0", md5="6bde2a6cef35d5732dfbb65ca3112d9e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
