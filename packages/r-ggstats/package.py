# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgstats(RPackage):
	"""Extension to 'ggplot2' for Plotting Stats

	Provides new statistics, new geometries and new positions for 
    'ggplot2' and a suite of functions to facilitate the creation of 
    statistical plots.
	"""
	
	homepage = "https://larmarange.github.io/ggstats/"
	cran = "ggstats" 

	version("0.5.1", md5="d615412a8c42e91abadd45f5d88c49a0")

	depends_on("r-broom-helpers@1.14:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
