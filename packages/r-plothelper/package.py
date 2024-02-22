# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlothelper(RPackage):
	"""New Plots Based on 'ggplot2' and Functions to Create Regular
Shapes

	An extension to 'ggplot2' and 'magick'. It contains 
    three groups of functions: Functions in the first group draw 'ggplot2' - based plots: geom_shading_bar() draws barplot 
	with shading colors in each bar. geom_rect_cm(), geom_circle_cm() and geom_ellipse_cm() draw rectangles, circles 
	and ellipses with centimeter as their unit. Thus their sizes do not change when the coordinate system or the aspect ratio 
	changes. annotation_transparent_text() draws labels with transparent texts. annotation_shading_polygon() draws irregular 
	polygons with shading colors. Functions in the second group generate coordinates for regular shapes and make linear transformations. Functions in the third group are 'magick' - based functions facilitating image processing.
	"""
	
	homepage = "https://github.com/githubwwwjjj/plothelper/blob/master/README.md"
	cran = "plothelper" 

	version("0.1.9", md5="11b88475b1983b4153ae05ab4a8cf663")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggfittext@0.8.1:", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-farver", type=("build", "run"))
