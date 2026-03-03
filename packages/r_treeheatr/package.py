# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeheatr(RPackage):
	"""Heatmap-Integrated Decision Tree Visualizations

	Creates interpretable decision tree visualizations 
    with the data represented as a heatmap at the tree's leaf nodes.
    'treeheatr' utilizes the customizable 'ggparty' package for 
    drawing decision trees.
	"""
	
	homepage = "https://trang1618.github.io/treeheatr/index.html"
	cran = "treeheatr" 

	version("0.2.1", md5="3741a7bb4a38ba4b4c323991ab8e570b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggparty", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
	depends_on("r-seriation", type=("build", "run"))
