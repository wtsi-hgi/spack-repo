# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgalt(RPackage):
	"""Extra Coordinate Systems, 'Geoms', Statistical Transformations,
Scales and Fonts for 'ggplot2'

	A compendium of new geometries, coordinate systems, statistical 
    transformations, scales and fonts for 'ggplot2', including splines, 1d and 2d densities, 
    univariate average shifted histograms, a new map coordinate system based on the 
    'PROJ.4'-library along with geom_cartogram() that mimics the original functionality of 
    geom_map(), formatters for "bytes", a stat_stepribbon() function, increased 'plotly'
    compatibility and the 'StateFace' open source font 'ProPublica'. Further new 
    functionality includes lollipop charts, dumbbell charts, the ability to encircle
    points and coordinate-system-based text annotations.
	"""
	
	homepage = "https://github.com/hrbrmstr/ggalt"
	cran = "ggalt" 

	version("0.4.0", md5="577a558a4d4edfb47160b64f6a3a951c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-proj4", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-ash", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-plotly@3.4.1:", type=("build", "run"))
