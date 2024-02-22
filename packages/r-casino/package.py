# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCasino(RPackage):
	"""Play Casino Games

	Play casino games in the R console,
  including poker, blackjack, and a slot machine.
  Try to build your fortune before you succumb to the gambler's ruin!
	"""
	
	homepage = "https://anthonypileggi.github.io/casino"
	cran = "casino" 

	version("0.1.0", md5="69393651e0072a0bc671f9b23704a60e")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
