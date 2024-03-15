# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfluencer(RPackage):
	"""Software Tools to Quantify Structural Importance of Nodes in a Network.

	Provides functionality to compute various node centrality measures on
	networks. Included are functions to compute betweenness centrality (by
	utilizing Madduri and Bader's SNAP library), implementations of Burt's
	constraint and effective network size (ENS) metrics, Borgatti's algorithm
	to identify key players, and Valente's bridging metric. On Unix systems,
	the betweenness, Key Players, and bridging implementations are parallelized
	with OpenMP, which may run faster on systems which have OpenMP
	configured."""

	cran = "influenceR"

	version("0.1.5", md5="7223e03ae2bc757205e4090cec9a8aee")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-matrix@1.1.4:", type=("build", "run"))
