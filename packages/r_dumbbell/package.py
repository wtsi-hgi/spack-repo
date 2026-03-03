# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDumbbell(RPackage):
	"""Displaying Changes Between Two Points Using Dumbbell Plots

	Creates a Dumbbell Plot.
	"""
	
	homepage = "https://github.com/foocheung2/dumbbell"
	cran = "dumbbell" 

	version("0.1", md5="bb254f8778b79ee7dcba9f1f62a7e94a")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
