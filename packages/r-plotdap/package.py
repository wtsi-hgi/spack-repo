# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotdap(RPackage):
	"""Easily Visualize Data from 'ERDDAP' Servers via the 'rerddap'
Package

	Easily visualize and animate 'tabledap' and 'griddap' objects obtained via the 'rerddap' package in a simple one-line command,  using either base graphics or 'ggplot2' graphics. 'plotdap' handles extracting and reshaping the data,  map projections and continental outlines.  Optionally the data can be animated through time using the 'gganmiate' package.
	"""
	
	homepage = "https://github.com/rmendels/plotdap"
	cran = "plotdap" 

	version("1.0.3", md5="ad2a340893eac0731cbd8d3871e96adb")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-cmocean", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mapdata", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rerddap@0.8:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
