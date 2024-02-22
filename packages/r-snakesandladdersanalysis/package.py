# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnakesandladdersanalysis(RPackage):
	"""Play and Analyse the Game of Snakes and Ladders

	Plays the game of Snakes and Ladders and has tools for analyses. The tools included allow you to find the average moves to win, frequency of each square, importance of the snakes and the ladders, the most common square and the plotting of the game played.
	"""
	
	cran = "SnakesAndLaddersAnalysis" 

	version("2.1.0", md5="ced698c7426280d9ce2a1533c710c588")

