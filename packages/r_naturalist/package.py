# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaturalist(RPackage):
	"""Classify Occurrences by Confidence Levels in the Species ID

	Classify occurrence records based on confidence
    levels of species identification. In addition, implement tools to filter
    occurrences inside grid cells and to manually check for possibles errors with 
	an interactive shiny application.
	"""
	
	homepage = "https://github.com/avrodrigues/naturaList"
	cran = "naturaList" 

	version("0.5.2", md5="dcd6d17ceb10884f194d29740e732f2d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-leaflet-extras", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-fasterize", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
