# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenrepgridIc(RPackage):
	"""Interpretive Clustering for Repertory Grids

	Shiny UI to identify cliques of related constructs in repertory grid data. 
    See Burr, King, & Heckmann (2020) <doi:10.1080/14780887.2020.1794088> for a description 
    of the interpretive clustering (IC) method.
	"""
	
	homepage = "https://github.com/markheckmann/OpenRepGrid.ic"
	cran = "OpenRepGrid.ic" 

	version("0.6.2", md5="07d9018bdb2eaf0cf88d0040d18b25f0")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinydashboardplus@2:", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
