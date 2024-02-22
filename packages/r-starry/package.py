# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarry(RPackage):
	"""Explore Data with Plots and Tables

	Provides modular functions and applications for quickly generating 
    plots and tables. Each modular function opens a graphical user interface 
    providing the user with options to create and customise plots and tables.
	"""
	
	homepage = "https://joe-chelladurai.github.io/starry/"
	cran = "starry" 

	version("0.1.2", md5="628677cd6689256bc4ecdcc6a8eb7678")

	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-corrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
