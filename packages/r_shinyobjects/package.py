# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyobjects(RPackage):
	"""Access Reactive Data Interactively

	Troubleshooting reactive data in 'shiny' can be difficult. These functions will convert reactive data frames into functions and load all assigned objects into your local environment. If you create a dummy input object, as the function will suggest, you will be able to test your server and ui functions interactively.
	"""
	
	cran = "shinyobjects" 

	version("0.2.0", md5="23c90f5c93c302f90fe6f4dd913a840f")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-styler", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
