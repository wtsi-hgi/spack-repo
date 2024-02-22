# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGissb(RPackage):
	"""Network Analysis on the Norwegian Road Network

	A collection of GIS (Geographic Information System) functions in R, created for use in Statistics Norway. The functions are primarily related to network analysis on the Norwegian road network. 
	"""
	
	homepage = "https://statisticsnorway.github.io/GISSB/"
	cran = "GISSB" 

	version("1.1", md5="db83a89c7afa2f8db21555a849e51424")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cpprouting", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
