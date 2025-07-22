# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiwgcna(RPackage):
	"""multiWGCNA

	An R package for deeping mining gene co-expression networks in multi-trait expression data. Provides functions for analyzing, comparing, and visualizing WGCNA networks across conditions. multiWGCNA was designed to handle the common case where there are multiple biologically meaningful sample traits, such as disease vs wildtype across development or anatomical region.
	"""
	
	bioc = "multiWGCNA"

	version("1.6.0", commit="a49a706cb8ec182bf10245dda54be46144d0056a")
	version("1.0.0", commit="cf072470816791d2edd1cd8daaa834961a39acf2")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggalluvial", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-flashclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dcanr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
