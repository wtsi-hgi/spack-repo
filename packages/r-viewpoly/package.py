# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViewpoly(RPackage):
	"""A Shiny App to Visualize Genetic Maps and QTL Analysis in
Polyploid Species

	Provides a graphical user interface to integrate, visualize and explore results 
            from linkage and quantitative trait loci analysis, together with genomic information for autopolyploid 
            species. The app is meant for interactive use and allows users to optionally upload different sources 
            of information, including  gene annotation and alignment files, enabling the exploitation and search for 
            candidate genes in a genome browser. In its current version, 'VIEWpoly' supports inputs from 'MAPpoly', 
            'polymapR', 'diaQTL', 'QTLpoly' and 'polyqtlR' packages. 
	"""
	
	homepage = "https://github.com/mmollina/viewpoly"
	cran = "viewpoly" 

	version("0.3.2", md5="8d97b56d225b63570da1aacaa52f873b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-golem@0.3.1:", type=("build", "run"))
	depends_on("r-jbrowser", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
