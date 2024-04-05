# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfm(RPackage):
	"""Recency, Frequency and Monetary Value Analysis

	Tools for RFM (recency, frequency and monetary value) analysis. 
    Generate RFM score from both transaction and customer level data. Visualize the
    relationship between recency, frequency and monetary value using heatmap, 
    histograms, bar charts and scatter plots. Includes a 'shiny' app for 
    interactive segmentation. References:
    i. Blattberg R.C., Kim BD., Neslin S.A (2008) <doi:10.1007/978-0-387-72579-6_12>.
	"""
	
	homepage = "https://github.com/rsquaredacademy/rfm"
	cran = "rfm" 

	version("0.3.0", md5="2704cebf5e71b675266143551a945dd7")
	version("0.2.2", md5="a033fa880397674eaad3abc7317ef274")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-treemapify", type=("build", "run"))
	depends_on("r-xplorerr", type=("build", "run"))
