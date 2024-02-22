# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevgadgets(RPackage):
	"""Visualization and Post-Processing of 'RevBayes' Analyses

	Processes and visualizes the output of complex phylogenetic analyses from the 'RevBayes' phylogenetic graphical modeling software.
	"""
	
	homepage = "https://github.com/revbayes/RevGadgets"
	cran = "RevGadgets" 

	version("1.2.1", md5="70cedf691d84e7b158331e326242b136")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ape@5.4:", type=("build", "run"))
	depends_on("r-phytools@0.7.70:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggtree@3.6.1:", type=("build", "run"))
	depends_on("r-tidytree@0.3.4:", type=("build", "run"))
	depends_on("r-treeio@1.12:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-reshape@0.8.8:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-gginnards@0.0.3:", type=("build", "run"))
	depends_on("r-ggplotify@0.0.5:", type=("build", "run"))
	depends_on("r-ggpp", type=("build", "run"))
	depends_on("r-ggimage", type=("build", "run"))
	depends_on("r-png@0.1.7:", type=("build", "run"))
	depends_on("r-deeptime@0.1:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
