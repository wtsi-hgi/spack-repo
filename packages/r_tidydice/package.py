# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidydice(RPackage):
	"""Simulates Dice Rolls and Coin Flips

	Utils for basic statistical experiments, that can be used for teaching 
    introductory statistics. Each experiment generates a tibble.
    Dice rolls and coin flips are simulated using sample().
    The properties of the dice can be changed, like the number of sides.
    A coin flip is simulated using a two sided dice.
    Experiments can be combined with the pipe-operator.
	"""
	
	homepage = "https://github.com/rolkra/tidydice"
	cran = "tidydice" 

	version("1.0.0", md5="8033578ee812b07ea918b3c885ca2dfc")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
