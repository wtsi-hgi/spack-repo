# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerk(RPackage):
	"""Predicting Environmental Concentration and Risk

	A Shiny Web Application to predict and visualize concentrations of pharmaceuticals in the aqueous environment. 
    Jagadeesan K., Barden R. and Kasprzyk-Hordern B. (2022) <https://www.ssrn.com/abstract=4306129>.
	"""
	
	homepage = "https://github.com/jkkishore85/PERK/"
	cran = "PERK" 

	version("0.0.9.2", md5="2aa66fcb4415db89e746cb6ed67ccebe")

	depends_on("r-bs4dash", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem@0.3.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
