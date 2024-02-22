# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCamelup(RPackage):
	"""'CamelUp' Board Game as a Teaching Aid for Introductory
Statistics

	Implements the board game 'CamelUp' for use in introductory statistics classes using a Shiny app. 
	"""
	
	cran = "CamelUp" 

	version("2.0.3", md5="8d85a7035279950be8040ed7f6938120")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
