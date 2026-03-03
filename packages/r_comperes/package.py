# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComperes(RPackage):
	"""Manage Competition Results

	Tools for storing and managing competition results.
    Competition is understood as a set of games in which players gain some
    abstract scores.  There are two ways for storing results: in long (one
    row per game-player) and wide (one row per game with fixed amount of
    players) formats. This package provides functions for creation and
    conversion between them. Also there are functions for computing their
    summary and Head-to-Head values for players. They leverage grammar of
    data manipulation from 'dplyr'.
	"""
	
	homepage = "https://github.com/echasnovski/comperes"
	cran = "comperes" 

	version("0.2.7", md5="a86195418cc53d54220f4c86010cd521")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@0.7:", type=("build", "run"))
