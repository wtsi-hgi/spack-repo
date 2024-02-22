# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdapaceshiny(RPackage):
	"""A Shiny App for the 'fdapace' Package

	Shiny app for the 'fdapace' package.
	"""
	
	homepage = "https://github.com/cpossinger/fdapaceShiny"
	cran = "fdapaceShiny" 

	version("1.0.5", md5="4b42a8eb15869988e3cb61d5780b201a")

	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem@0.3.1:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bs4dash", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
