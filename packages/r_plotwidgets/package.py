# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotwidgets(RPackage):
	"""Spider Plots, ROC Curves, Pie Charts and More for Use in Other
Plots

	Small self-contained plots for use in larger plots or to
    delegate plotting in other functions. Also contains a number of
    alternative color palettes and HSL color space based tools to modify
    colors or palettes.
	"""
	
	cran = "plotwidgets" 

	version("0.5.1", md5="0711568192bcf77eab732aa5c1bc999d")

