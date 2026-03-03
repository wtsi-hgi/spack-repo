# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThewitcher(RPackage):
	"""Palettes Inspired by the TV Show "The Witcher"

	Plot your data using color palettes for 'ggplot2' inspired by the TV show, book series and video games "The Witcher".
	"""
	
	cran = "thewitcher" 

	version("1.0.1", md5="2581bca23651dc5781860fbd7b10bb1c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
