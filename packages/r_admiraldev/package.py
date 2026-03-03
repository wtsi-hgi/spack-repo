# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmiraldev(RPackage):
	"""Utility Functions and Development Tools for the Admiral Package
Family

	Utility functions to check data, variables and conditions for functions used in
 'admiral' and 'admiral' extension packages.  Additional utility helper functions to assist developers 
 with maintaining documentation, testing and general upkeep of 'admiral' and 'admiral' extension packages.  
	"""
	
	homepage = "https://pharmaverse.github.io/admiraldev/"
	cran = "admiraldev" 

	version("1.0.0", md5="7a987dffeb0abae0486fbab264899ccf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-hms@0.5.3:", type=("build", "run"))
	depends_on("r-lifecycle@0.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
