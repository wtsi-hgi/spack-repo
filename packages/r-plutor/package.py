# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlutor(RPackage):
	"""Useful Functions for Visualization

	In ancient Roman mythology, 'Pluto' was the ruler of the underworld
  and presides over the afterlife. 'Pluto' was frequently conflated with 
  'Plutus', the god of wealth, because mineral wealth was found underground. 
  When plotting with R, you try once, twice, practice again and again, and finally 
  you get a pretty figure you want. It's a 'plot tour', a tour about repetition 
  and reward. Hope 'plutor' helps you on the tour!
	"""
	
	homepage = "https://github.com/william-swl/plutor"
	cran = "plutor" 

	version("0.1.0", md5="8d09c3c5222983791b0e79d1f43d7e39")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-baizer", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggh4x", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-repr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
