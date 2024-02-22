# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaffsim(RPackage):
	"""Simulation of Plasma Caffeine Concentrations by Using Population
Pharmacokinetic Model

	Simulate plasma caffeine concentrations using population pharmacokinetic model described in Lee, Kim, Perera, McLachlan and Bae (2015) <doi:10.1007/s00431-015-2581-x>.
	"""
	
	homepage = "https://github.com/asancpt/caffsim"
	cran = "caffsim" 

	version("0.2.2", md5="2edc524e725a88745d50ab23e1b13800")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
