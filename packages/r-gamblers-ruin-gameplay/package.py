# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamblersRuinGameplay(RPackage):
	"""One-Dimensional Random Walks Through Simulation of the Gambler's
Ruin Problem

	Simulates a gambling game under the gambler's ruin setup, after asking for the money you have and the money you want to win, along with your win probability in each round of the game.
	"""
	
	cran = "gamblers.ruin.gameplay" 

	version("4.0.5", md5="454afd8073c51d1d300339d5051ca885")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hrbrthemes", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
