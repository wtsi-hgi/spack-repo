# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscover(RPackage):
	"""Exploratory Data Analysis System

	Performs an exploratory data analysis through a 'shiny' interface. It includes basic methods such as the mean, median, mode, normality test, among others. It also includes clustering techniques such as Principal Components Analysis, Hierarchical Clustering and the K-Means Method.
	"""
	
	homepage = "https://www.promidat.com"
	cran = "discoveR" 

	version("3.1.2", md5="e9347a8cff98ae13cb164be78a877951")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-shiny@1.7.4:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-loader", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-echarts4r", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinycustomloader", type=("build", "run"))
	depends_on("r-shinydashboardplus@2:", type=("build", "run"))
