# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonobinshiny(RPackage):
	"""Shiny User Interface for 'monobin' Package

	This is an add-on package to the 'monobin' package that simplifies its use. It provides shiny-based user interface (UI) 
	     that is especially handy for less experienced 'R' users as well as for those who intend to perform quick scanning 
	     of numeric risk factors when building credit rating models. The additional functions implemented in 
	     'monobinShiny' that do no exist in 'monobin' package are: descriptive statistics, special case and outliers imputation. 
	     The function descriptive statistics is exported and can be used in 'R' sessions independently from the user interface, 
	     while special case and outlier imputation functions are written to be used with shiny UI.
	"""
	
	homepage = "https://github.com/andrija-djurovic/monobinShiny"
	cran = "monobinShiny" 

	version("0.1.0", md5="c3039b47df51b88d184395f6d5a7cfef")

	depends_on("r-dt", type=("build", "run"))
	depends_on("r-monobin", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
