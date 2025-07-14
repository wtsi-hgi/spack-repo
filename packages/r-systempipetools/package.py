# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSystempipetools(RPackage):
	"""Tools for data visualization

	systemPipeTools package extends the widely used systemPipeR (SPR) workflow environment with an enhanced toolkit for data visualization, including utilities to automate the data visualizaton for analysis of differentially expressed genes (DEGs). systemPipeTools provides data transformation and data exploration functions via scatterplots, hierarchical clustering heatMaps, principal component analysis, multidimensional scaling, generalized principal components, t-Distributed Stochastic Neighbor embedding (t-SNE), and MA and volcano plots. All these utilities can be integrated with the modular design of the systemPipeR environment that allows users to easily substitute any of these features and/or custom with alternatives.
	"""
	
	bioc = "systemPipeTools"

	version("1.16.0", commit="b73e58c3afc7f1d8ae9f3894531512290a65914b")
	version("1.10.0", commit="41d021a31b356de23c8b566176d3fb3ae629e8c4")

	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-glmpca", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
