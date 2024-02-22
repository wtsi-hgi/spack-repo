# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupportr(RPackage):
	"""Support Functions for Wrangling and Visualization

	Suite of helper functions for data wrangling and visualization.
    The only theme for these functions is that they tend towards simple, short, and narrowly-scoped.
    These functions are built for tasks that often recur but are not large enough in scope to warrant an ecosystem of interdependent functions.
	"""
	
	cran = "supportR" 

	version("1.2.0", md5="ad6edd19891d50476d568c8d41b0b7e0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-googledrive", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
