# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyrecipes(RPackage):
	"""Gadget to Use the Data Preprocessing 'recipes' Package
Interactively

	This gadget allows you to use the 'recipes' package belonging to 'tidymodels' to carry 
    out the data preprocessing tasks in an interactive way. Build your 'recipe' by dragging the variables, 
    visually analyze your data to decide which steps to use, add those steps and preprocess your data.
	"""
	
	homepage = "https://github.com/AlbertoAlmuinha/shinyrecipes"
	cran = "shinyrecipes" 

	version("0.1.0", md5="91eab39d735612785777f763247fc14d")

	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinyglide", type=("build", "run"))
	depends_on("r-sortable", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-esquisse", type=("build", "run"))
