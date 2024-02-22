# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPomdpsolve(RPackage):
	"""Interface to 'pomdp-solve' for Partially Observable Markov
Decision Processes

	Installs an updated version of 'pomdp-solve', a program to solve Partially Observable Markov Decision Processes (POMDPs) using a variety of exact and approximate value iteration algorithms. A convenient R infrastructure is provided in the separate package pomdp. Kaelbling, Littman and Cassandra (1998) <doi:10.1016/S0004-3702(98)00023-X>.
	"""
	
	homepage = "https://github.com/mhahsler/pomdpSolve"
	cran = "pomdpSolve" 

	version("1.0.4", md5="c90412a7d3821318679957a040895c98")

	depends_on("r@3.5:", type=("build", "run"))
