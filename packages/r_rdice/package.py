# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdice(RPackage):
	"""A Collection of Functions to Experiment Dice Rolls

	A collection of functions to simulate
  dice rolls and the like. In particular, experiments and exercises can
  be performed looking at combinations and permutations of values in dice
  rolls and coin flips, together with the corresponding frequencies of
  occurrences. When applying each function, the user has to input the
  number of times (rolls, flips) to toss the dice. Needless to say, the more
  the tosses, the more the frequencies approximate the actual probabilities.
  Moreover, the package provides functions to generate non-transitive sets
  of dice (like Efron's) and to check whether a given set of dice is non-transitive
  with given probability.
	"""
	
	cran = "Rdice" 

	version("1.0.0", md5="2358db318547df51f613677cac30876d")

	depends_on("r-data-table", type=("build", "run"))
