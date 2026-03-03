# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAddinsoutline(RPackage):
	"""'RStudio' Addins for Show Outline of a R Markdown/'LaTeX'
Project

	'RStudio' allows to show and navigate for the outline of a 
    R Markdown file, but not for R Markdown projects with multiple 
    files. For this reason, I have developed several 'RStudio' addins capable 
    of show project outline. Each addin is specialized in showing projects 
    of different types: R Markdown project, 'bookdown' package project 
    and 'LaTeX' project. There is a configuration file that allows you 
    to customize additional searches.
	"""
	
	homepage = "https://github.com/calote/addinsOutline"
	cran = "addinsOutline" 

	version("0.1.6", md5="31cb6b3d2484a2ec6179a8218827b4ce")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-miniui@0.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
	depends_on("r-shinyfiles@0.7.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr@0.7.7:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
