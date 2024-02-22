# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcl(RPackage):
	"""Markov Cluster Algorithm

	Contains the Markov cluster algorithm (MCL) for identifying clusters in networks and graphs. The algorithm simulates random walks on a (n x n) matrix as the adjacency matrix of a graph. It alternates an expansion step and an inflation step until an equilibrium state is reached.
	"""
	
	cran = "MCL" 

	version("1.0", md5="c058c91e0910288a5e46a90ec954e34f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
