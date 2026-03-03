# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantedaTextplots(RPackage):
	"""Plots for the Quantitative Analysis of Textual Data

	Plotting functions for visualising textual data.  Extends 'quanteda' and 
   related packages with plot methods designed specifically for text data, textual statistics, 
   and models fit to textual data. Plot types include word clouds, lexical dispersion plots, 
   scaling plots, network visualisations, and word 'keyness' plots.
	"""
	
	cran = "quanteda.textplots" 

	version("0.94.4", md5="6536ae8bd0b8ae7aebc177434cd59db1")

	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
