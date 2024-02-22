# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordpuzzler(RPackage):
	"""Word Puzzle Game

	The word puzzle game requires you to find out the letters in a word within a limited number of guesses. In each round, if your guess hit any letters in the word, they reveal themselves. If all letters are revealed before your guesses run out, you win this game; otherwise you fail. You may run multiple games to guess different words.
	"""
	
	cran = "wordPuzzleR" 

	version("0.1.0", md5="9c6b6ca47226916d30cdf18002b54fdc")

	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
