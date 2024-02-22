# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoardgames(RPackage):
	"""Board Games and Tools for Building Board Games

	Tools for constructing board/grid based games, as well as readily available game(s) for your entertainment.
	"""
	
	cran = "BoardGames" 

	version("1.0.0", md5="327294b945543264d09b1c99cb803ccb")

	depends_on("r@3.0.2:", type=("build", "run"))
