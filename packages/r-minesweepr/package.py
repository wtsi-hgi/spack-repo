# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinesweepr(RPackage):
	"""Mine Sweeper Game

	This is the very popular mine sweeper game! The game requires you to find out tiles that contain mines through clues from unmasking neighboring tiles. Each tile that does not contain a mine shows the number of mines in its adjacent tiles. If you unmask all tiles that do not contain mines, you win the game; if you unmask any tile that contains a mine, you lose the game. For further game instructions, please run `help(run_game)` and check details. This game runs in X11-compatible devices with `grDevices::x11()`.
	"""
	
	cran = "mineSweepR" 

	version("0.1.1", md5="47ccd524d39f6f056a8973ff2277d59d")

	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-interactivecomplexheatmap", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gsignal", type=("build", "run"))
	depends_on("r-mgc", type=("build", "run"))
	depends_on("r-mmand", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-pals", type=("build", "run"))
