# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArena2r(RPackage):
	"""Plots, Summary Statistics and Tools for Arena Simulation Users

	Reads Arena <https://www.arenasimulation.com/> CSV output files and generates nice tables and plots. The package contains a Shiny App that can be used to interactively visualize Arena's results.
	"""
	
	homepage = "https://github.com/pedroliman/arena2r"
	cran = "arena2r" 

	version("1.0.0", md5="f856d40b0a5daa4b4da2174c04de88db")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
