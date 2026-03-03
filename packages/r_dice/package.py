# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDice(RPackage):
	"""Calculate probabilities of various dice-rolling events

	This package provides utilities to calculate the probabilities of various dice-rolling events, such as the probability of rolling a four-sided die six times and getting a 4, a 3, and either a 1 or 2 among the six rolls (in any order); the probability of rolling two six-sided dice three times and getting a 10 on the first roll, followed by a 4 on the second roll, followed by anything but a 7 on the third roll; or the probabilities of each possible sum of rolling five six-sided dice, dropping the lowest two rolls, and summing the remaining dice.
	"""
	
	cran = "dice" 

	version("1.2", md5="a78712062d31629090f1af6c6440c969")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
