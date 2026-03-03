# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetshiny(RPackage):
	"""Tool for Comparison and Visualization of Multiple Networks

	We developed a comprehensive tool that helps with visualization and analysis of networks with the same variables across multiple factor levels. The 'netShiny' contains most of the popular network features such as centrality measures, modularity, and other summary statistics (e.g. clustering coefficient). It also contains known tools to look at the (dis)similarities between two networks, such as pairwise distance measures between networks, set operations on the nodes of the networks, distribution of the weights of the edges and a network representing the difference between two correlation matrices. The package 'netShiny' also contains tools to perform bootstrapping and find clusters in networks. See the 'netShiny' manual for more information, documentation and examples.
	"""
	
	cran = "netShiny" 

	version("1.0", md5="1038108542d4db40a094c870236cf69c")

	depends_on("r-shinybs@0.61.1:", type=("build", "run"))
	depends_on("r-shiny@1.7.2:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7.2:", type=("build", "run"))
	depends_on("r-colourpicker@1.1.1:", type=("build", "run"))
	depends_on("r-dt@0.24:", type=("build", "run"))
	depends_on("r-future@1.27:", type=("build", "run"))
	depends_on("r-future-callr@0.8:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-ggvenndiagram@1.2:", type=("build", "run"))
	depends_on("r-igraph@1.3.4:", type=("build", "run"))
	depends_on("r-ipc@0.1.3:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-matrix@1.4.1:", type=("build", "run"))
	depends_on("r-netgwas@1.14:", type=("build", "run"))
	depends_on("r-plotly@4.10:", type=("build", "run"))
	depends_on("r-promises@1.2.0.1:", type=("build", "run"))
	depends_on("r-readxl@1.4:", type=("build", "run"))
	depends_on("r-shinycssloaders@1:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-shinyscreenshot@0.2:", type=("build", "run"))
	depends_on("r-shinywidgets@0.7.2:", type=("build", "run"))
	depends_on("r-visnetwork@2.1:", type=("build", "run"))
