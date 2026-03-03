# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLexisplotr(RPackage):
	"""Plot Lexis Diagrams for Demographic Purposes

	Plots empty Lexis grids, adds lifelines and highlights certain areas of the grid, like cohorts and age groups.
	"""
	
	homepage = "https://github.com/ottlngr/LexisPlotR"
	cran = "LexisPlotR" 

	version("0.4.0", md5="83271a8623467da2bd2b9134587ae6f4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
