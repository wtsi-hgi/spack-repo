# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProton(RPackage):
	"""The Proton Game

	'The Proton Game' is a console-based data-crunching game for younger and older data scientists.
  Act as a data-hacker and find Slawomir Pietraszko's credentials to the Proton server.
  You have to solve four data-based puzzles to find the login and password.
  There are many ways to solve these puzzles. You may use loops, data filtering, ordering, aggregation or other tools.
  Only basics knowledge of R is required to play the game, yet the more functions you know, the more approaches you can try.
  The knowledge of dplyr is not required but may be very helpful.
  This game is linked with the ,,Pietraszko's Cave'' story available at http://biecek.pl/BetaBit/Warsaw.
  It's a part of Beta and Bit series.
  You will find more about the Beta and Bit series at http://biecek.pl/BetaBit.
	"""
	
	cran = "proton" 

	version("1.0", md5="b09548fb8bee038f9ecba2d20f27e0eb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
