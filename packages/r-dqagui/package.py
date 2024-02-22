# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDqagui(RPackage):
	"""Graphical User Interface for Data Quality Assessment

	A graphical user interface (GUI) to the functions implemented in the R package 'DQAstats'. Publication: Mang et al. (2021) <doi:10.1186/s12911-022-01961-z>.
	"""
	
	homepage = "https://github.com/miracum/dqa-dqagui"
	cran = "DQAgui" 

	version("0.2.3", md5="6bfda8b45630d965e76b31d64c886df8")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-daterangepicker", type=("build", "run"))
	depends_on("r-diztools@0.0.5:", type=("build", "run"))
	depends_on("r-dizutils@0.1.1:", type=("build", "run"))
	depends_on("r-dqastats@0.3.1:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
