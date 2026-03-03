# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTictactoe(RPackage):
	"""Tic-Tac-Toe Game

	
  Implements tic-tac-toe game to play on console, either with human or AI players.
  Various levels of AI players are trained through the Q-learning algorithm.
	"""
	
	homepage = "https://github.com/kota7/tictactoe"
	cran = "tictactoe" 

	version("0.2.2", md5="1bd38351dfa38e6afcc4f04298bb7ec9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
