# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGimmemyplot(RPackage):
	"""Graphical Utilities for Visualizing and Exploring Data

	Simplifies the process of creating essential visualizations
    in R, offering a range of plotting functions for common chart types
    like violin plots, pie charts, and histograms.  With an intuitive
    interface, users can effortlessly customize colors, labels, and
    styles, making it an ideal tool for both beginners and experienced
    data analysts. Whether exploring datasets or producing quick visual
    summaries, this package provides a streamlined solution for
    fundamental graphics in R.
	"""
	
	cran = "GimmeMyPlot" 

	version("0.1.0", md5="15d9ee5bb921f95b03360d715cd7218e")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
