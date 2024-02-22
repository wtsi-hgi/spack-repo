# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkgen(RPackage):
	"""Network Maze Generator

	A network Maze generator that creates different types of network mazes. 
	"""
	
	cran = "networkGen" 

	version("0.1.1", md5="1a11f156342ce56977582992d594c7c4")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
