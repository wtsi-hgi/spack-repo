# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExplor(RPackage):
	"""Interactive Interfaces for Results Exploration

	Shiny interfaces and graphical functions for multivariate analysis results exploration.
	"""
	
	homepage = "https://juba.github.io/explor/"
	cran = "explor" 

	version("0.3.10", md5="ee6997e3dd3e744191cb769b6d54d26a")

	depends_on("r-shiny@1:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-highr", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-scatterd3@1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
