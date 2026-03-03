# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabulator(RPackage):
	"""Efficient Tabulation with Stata-Like Output

	Efficient tabulation with Stata-like output.
	For each unique value of the variable, it shows the number of 
	observations with that value, proportion of observations with that
	value, and cumulative proportion, in descending order of frequency.
	Accepts data.table, tibble, or data.frame as input. 
	Efficient with big data: if you give it a data.table, 
	tab() uses data.table syntax.
	"""
	
	cran = "tabulator" 

	version("1.0.0", md5="97a74a818fc5d962e2d984155dc8cf20")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
