# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REufmdisAdapt(RPackage):
	"""Analyse 'EuFMDiS' Output Files via a Shiny App

	Analyses 'EuFMDiS' output files in a Shiny App. The distributions of 
  relevant output parameters are described in form of tables (quantiles) and plots. 
  The App is called using eufmdis.adapt::run_adapt().
	"""
	
	cran = "eufmdis.adapt" 

	version("0.1.0", md5="14e9ab3ee94b63fed3ff77e0febda5d9")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
