# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamesga(RPackage):
	"""Genetic Algorithm for Sequential Symmetric Games

	Finds adaptive strategies for sequential symmetric 
    games using a genetic algorithm. Currently, any symmetric two by two matrix
    is allowed, and strategies can remember the history of an opponent's play
    from the previous three rounds of moves in iterated interactions between
    players. The genetic algorithm returns a list of adaptive strategies given
    payoffs, and the mean fitness of strategies in each generation.
	"""
	
	homepage = "https://bradduthie.github.io/gamesGA/"
	cran = "gamesGA" 

	version("1.1.3.7", md5="72c1834b7b98e32aef5952076ca9b72c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-shiny@1:", type=("build", "run"))
