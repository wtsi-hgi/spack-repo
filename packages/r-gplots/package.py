# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGplots(RPackage):
	"""Various R Programming Tools for Plotting Data.

	Various R programming tools for plotting data, including:
	[1] calculating and plotting locally smoothed summary function as
	('bandplot', 'wapply'),
	[2] enhanced versions of standard plots ('barplot2', 'boxplot2',
	'heatmap.2', 'smartlegend'),
	[3] manipulating colors ('col2hex', 'colorpanel', 'redgreen', 'greenred',
	'bluered', 'redblue', 'rich.colors'),
	[4] calculating and plotting two-dimensional data summaries ('ci2d',
	'hist2d'),
	[5] enhanced regression diagnostic plots ('lmplot2', 'residplot'),
	[6] formula-enabled interface to 'stats::lowess' function ('lowess'),
	[7] displaying textual data in plots ('textplot', 'sinkplot'),
	[8] plotting a matrix where each cell contains a dot whose size reflects
	the relative magnitude of the elements ('balloonplot'),
	[9] plotting "Venn" diagrams ('venn'),
	[10] displaying Open-Office style plots ('ooplot'),
	[11] plotting multiple data on same region, with separate axes
	('overplot'),
	[12] plotting means and confidence intervals ('plotCI', 'plotmeans'),
	[13] spacing points in an x-y plot so they don't overlap ('space')."""

	cran = "gplots"

	version("3.1.3.1", md5="4dd687c541fb88500ea28d9f4161f0b6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
