# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRchivaltag(RPackage):
	"""Analyzing and Interactive Visualization of Archival Tagging Data

	A set of functions to generate, access and analyze standard data products from archival tagging data.
	"""
	
	cran = "RchivalTag" 

	version("0.1.9", md5="0ce5ea38d1881d3d519fbfdc44efd610")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-mapdata", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-oceanmap", type=("build", "run"))
	depends_on("r-cleangeo", type=("build", "run"))
	depends_on("r-suntools", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggedit", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-leaflet-extras2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
