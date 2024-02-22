# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinytempsignal(RPackage):
	"""Explore Temporal and Other Phylogenetic Signals

	Sequences sampled at different time points can be used to infer molecular phylogenies on natural time scales, but if the sequences records inaccurate sampling times, that are not the actual sampling times, then it will affect the molecular phylogenetic analysis. This shiny application helps exploring temporal characteristics of the evolutionary trees through linear regression analysis and with the ability to identify and remove incorrect labels. The method was extended to support exploring other phylogenetic signals under strict and relaxed models.
	"""
	
	homepage = "https://github.com/YuLab-SMU/shinyTempSignal"
	cran = "shinyTempSignal" 

	version("0.0.7", md5="da8562e52a422395adc52737ad14d2ec")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggprism", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-golem@0.3.1:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-treeio", type=("build", "run"))
	depends_on("r-yulab-utils@0.1.4:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
