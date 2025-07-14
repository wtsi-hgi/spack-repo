# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetzoor(RPackage):
	"""Unified methods for the inference and analysis of gene regulatory networks

	netZooR unifies the implementations of several Network Zoo methods (netzoo, netzoo.github.io) into a single package by creating interfaces between network inference and network analysis methods. Currently, the package has 3 methods for network inference including PANDA and its optimized implementation OTTER (network reconstruction using mutliple lines of biological evidence), LIONESS (single-sample network inference), and EGRET (genotype-specific networks). Network analysis methods include CONDOR (community detection), ALPACA (differential community detection), CRANE (significance estimation of differential modules), MONSTER (estimation of network transition states). In addition, YARN allows to process gene expresssion data for tissue-specific analyses and SAMBAR infers missing mutation data based on pathway information.
	"""
	
	homepage = "https://github.com/netZoo/netZooR"
	bioc = "netZooR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/netZooR_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/netZooR/netZooR_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="7079477eb6f06b23cbd52441254ce3441f3b7e39e3923af01e9152d7f20e78ba")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-pandar", type=("build", "run"))
	depends_on("r-yarn", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-stringdb", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
