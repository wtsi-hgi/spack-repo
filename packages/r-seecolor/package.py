# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeecolor(RPackage):
	"""View Colors Used in R Objects in the Console

	Output colors used in literal vectors, palettes and plot objects (ggplot).
	"""
	
	homepage = "https://github.com/lovestat/seecolor"
	cran = "seecolor" 

	version("0.2.0", md5="262d27186d660e74f43addfb502fdf04")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-fansi", type=("build", "run"))
