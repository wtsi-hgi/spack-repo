# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrimeutils(RPackage):
	"""A Comprehensive Set of Functions to Clean, Analyze, and Present
Crime Data

	A collection of functions that make it easier to understand crime (or other)
    data, and assist others in understanding it. The package helps you read data 
    from various sources, clean it, fix column names, and graph the data. 
	"""
	
	homepage = "https://github.com/jacobkap/crimeutils/"
	cran = "crimeutils" 

	version("0.5.1", md5="d612bb14ba21a588412953a47b4431b4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
