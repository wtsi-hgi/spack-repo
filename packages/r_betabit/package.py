# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetabit(RPackage):
	"""Mini Games from Adventures of Beta and Bit

	Three games: proton, frequon and regression. Each one is a console-based data-crunching game for younger and older data scientists.
  Act as a data-hacker and find Slawomir Pietraszko's credentials to the Proton server.
  In proton you have to solve four data-based puzzles to find the login and password.
  There are many ways to solve these puzzles. You may use loops, data filtering, ordering, aggregation or other tools.
  Only basics knowledge of R is required to play the game, yet the more functions you know, the more approaches you can try.
  In frequon you will help to perform statistical cryptanalytic attack on a corpus of ciphered messages.
  This time seven sub-tasks are pushing the bar much higher. Do you accept the challenge?
  In regression you will test your modeling skills in a series of eight sub-tasks.
  Try only if ANOVA is your close friend.
  It's a part of Beta and Bit project.
  You will find more about the Beta and Bit project at <https://github.com/BetaAndBit/Charts>.
	"""
	
	homepage = "https://github.com/BetaAndBit/Charts"
	cran = "BetaBit" 

	version("2.2", md5="c295faf26422f587e70e6cdf05268c6e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
