# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REoffice(RPackage):
	"""Export or Graph and Tables to 'Microsoft' Office and Import
Figures and Tables

	Provides wrap functions to export and import graphics and
             data frames in R to 'microsoft' office. And This package also 
             provide write out figures with lots of different formats.
             Since people may work on the platform without GUI support, the package 
             also provide function to easily write out figures
             to lots of different type of formats. Now this package provide function 
             to extract colors from all types of figures and pdf files.
	"""
	
	cran = "eoffice" 

	version("0.2.2", md5="b74918cd6c0668b4feef001283ef3bdb")

	depends_on("r-officer", type=("build", "run"))
	depends_on("r-rvg", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-r-devices", type=("build", "run"))
	depends_on("r-devemf", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
