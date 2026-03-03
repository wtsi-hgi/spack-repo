# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarsexplore(RPackage):
	"""Searchable Variable Explorer with Labelled Variables

	Creates a summary dataframe that can be used in 'RStudio' similar to the variable
    explorer in 'Stata', but which also includes the summary statistics. By default the result 
    is shown in the 'RStudio' Viewer Pane as a searchable data table. This is useful particularly 
    if you have a large dataset with a very large number of labelled variables with hard to 
    remember names. Can also be used to generate a table of summary statistics.
	"""
	
	cran = "varsExplore" 

	version("0.3.0", md5="5e0f557a6345da43e9859c992ae8e764")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
