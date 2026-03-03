# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtsr(RPackage):
	"""Hydro-Meteorology Time-Series

	Functions for the management and treatment of hydrology and 
  meteorology time-series stored in a 'Sqlite' data base.
	"""
	
	homepage = "https://github.com/p-chevallier/htsr"
	cran = "htsr" 

	version("2.1.4", md5="dadeafa8b12a976abe6b2d15294739d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
	depends_on("r-writexls", type=("build", "run"))
