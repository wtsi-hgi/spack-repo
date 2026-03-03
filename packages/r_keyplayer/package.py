# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeyplayer(RPackage):
	"""Locating Key Players in Social Networks

	Computes group centrality scores and identifies the most central group of players in a network.
	"""
	
	cran = "keyplayer" 

	version("1.0.4", md5="95c56284f4a37e2d4f20ad6361d3c056")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-matpow", type=("build", "run"))
