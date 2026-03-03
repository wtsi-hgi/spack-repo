# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgorrr(RPackage):
	"""A Shiny Interface for Simple Data Management

	
  Launches a shiny application generating code to
    view tables in several ways,
    import/export tables,
    modify tables,
    make some basic graphics.
  'IGoR' is a graphic user interface designed to help beginners
  using simple functions around table management and exploration.
  Inspired by 'Rcmdr', 'IGoR' is a code generator that, with simple inputs under a Shiny application,
  provides R code mainly built around the 'tidyverse' or some packages in the direct line of the Mosaic project:
  the 'rio' and 'ggformula' packages.
  The generated code doesn't depend on IGoR and can be manually modified by the user or copied elsewhere.
	"""
	
	cran = "IGoRRR" 

	version("0.3.4", md5="8b40f50709b08cb6f4852d1b81eda6bd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-sortable", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-fuzzyjoin", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-feather", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-readods", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-skimr", type=("build", "run"))
	depends_on("r-tables", type=("build", "run"))
	depends_on("r-ggformula", type=("build", "run"))
	depends_on("r-mapsf", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
