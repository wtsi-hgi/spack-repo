# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMargaret(RPackage):
	"""Scientometric Analysis Minciencias

	The target of 'margaret' is help to extract data from Minciencias to analyze scientific production in Colombia.
	"""
	
	homepage = "https://github.com/coreofscience/margaret"
	cran = "margaret" 

	version("0.1.4", md5="89dc7c29fd3d0d4d72988f4bca467176")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-scholar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-treemapify", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-widyr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
