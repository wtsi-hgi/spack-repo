# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhosr(RPackage):
	"""A set of methods and tools for comprehensive analysis of phosphoproteomics data

	PhosR is a package for the comprenhensive analysis of phosphoproteomic data. There are two major components to PhosR: processing and downstream analysis. PhosR consists of various processing tools for phosphoproteomics data including filtering, imputation, normalisation, and functional analysis for inferring active kinases and signalling pathways.
	"""
	
	bioc = "PhosR"

	version("1.18.1", commit="7a08968efd8bd13aa9f1ef4fbe7c01d0f1d21210")
	version("1.12.0", commit="dfab942faba8000214d1e8c17702f73328018861")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ruv", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
