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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PhosR_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PhosR/PhosR_1.12.0.tar.gz"]

	version("1.18.1", tag="RELEASE_3_21")
	version("1.12.0", sha256="eb6c62944a7f9393b63aff148dd2bc8750f75cec5b7528fe6f7c0a03226056f2")

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
