# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvgtools(RPackage):
	"""Manipulate SVG (Template) Files of Charts

	The purpose of this package is to manipulate SVG files that are templates of charts the user wants to produce. 
    In vector graphics one copes with x-/y-coordinates of elements (e.g. lines, rectangles, text). Their scale is often dependent on the program that is used to produce the graphics. 
    In applied statistics one usually has numeric values on a fixed scale (e.g. percentage values between 0 and 100) to show in a chart. 
    Basically, 'svgtools' transforms the statistical values into coordinates and widths/heights of the vector graphics.
    This is done by stackedBar() for bar charts, by linesSymbols() for charts with lines and/or symbols (dot markers) and scatterSymbols() for scatterplots.
	"""
	
	cran = "svgtools" 

	version("1.1.0", md5="43daff2ccdf38a9b71f91c09ed35cff4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xml2@1.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-rsvg@2.1:", type=("build", "run"))
	depends_on("r-magick@2.4:", type=("build", "run"))
