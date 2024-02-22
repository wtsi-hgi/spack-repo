# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPieglyph(RPackage):
	"""Axis Invariant Scatter Pie Plots

	Extends 'ggplot2' to help replace points in a scatter plot with pie-chart glyphs showing the relative proportions of different categories. The pie glyphs are independent of the axes and plot dimensions, to prevent distortions when the plot dimensions are changed.
	"""
	
	homepage = "https://github.com/rishvish/PieGlyph"
	cran = "PieGlyph" 

	version("0.1.0", md5="08b86360a7750f8c0892061f5e307bf9")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
