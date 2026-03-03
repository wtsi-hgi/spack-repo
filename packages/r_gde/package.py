# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGde(RPackage):
	"""GBIF Dataset Explorer

	Functions to explore datasets from the Global Biodiversity Information Facility (GBIF - <https://www.gbif.org/>) using a Shiny interface.
	"""
	
	homepage = "https://github.com/Smithsonian/GBIF-Dataset-Explorer"
	cran = "gde" 

	version("0.2.1", md5="5894c9e9747e37e34eee9dd8e3f49517")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
