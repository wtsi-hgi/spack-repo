# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwalkr(RPackage):
	"""Interactive Exploratory Data Analysis Tool

	Simplify your R data analysis and data visualization workflow by turning your data frame into an interactive 'Tableau'-like interface, leveraging the 'graphic-walker' JavaScript library and the 'htmlwidgets' package.
	"""
	
	homepage = "https://github.com/Kanaries/GWalkR/"
	cran = "GWalkR" 

	version("0.1.3", md5="bc12e9c56f85fb4c8b52d00fc6383137")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
