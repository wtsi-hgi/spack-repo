# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorrrd(RPackage):
	"""Generate Wordsearch and Crossword Puzzles

	Generate wordsearch and crossword puzzles using
    custom lists of words (and clues).  Make them easy or hard,
    and print them to solve offline with paper and pencil!
	"""
	
	homepage = "https://www.stochastic-squirrel.com/worrrd/"
	cran = "worrrd" 

	version("0.1.0", md5="6f5392df2a49f18d2bdfc44510ab4964")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
