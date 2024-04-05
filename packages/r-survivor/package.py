# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivor(RPackage):
	"""Data from all Seasons of Survivor (US) TV Series in Tidy Format

	Several datasets which detail the results and events of each season of Survivor. This includes 
  details on the cast, voting history, immunity and reward challenges, jury votes and viewers. This data is 
  useful for practicing data wrangling, graph analytics and analysing how each season of Survivor played out. 
  Includes 'ggplot2' scales and colour palettes for visualisation.
	"""
	
	homepage = "https://github.com/doehm/survivoR"
	cran = "survivoR" 

	version("2.3.2", md5="89cac38bb1680ca8e741cff2db0bba2d")
	version("2.3.1", md5="30d35c58d8802d57fbdb710a772d15c7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
