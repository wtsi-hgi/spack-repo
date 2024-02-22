# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrepertoire(RPackage):
	"""A toolkit for single-cell immune receptor profiling

	scRepertoire was built to process data derived from the 10x Genomics Chromium Immune Profiling for both T-cell receptor (TCR) and immunoglobulin (Ig) enrichment workflows and subsequently interacts with the popular Seurat and SingleCellExperiment R packages. It also allows for general analysis of single-cell clonotype information without the use of expression information. The package functions as a wrapper for Startrac and powerTCR R packages.
	"""
	
	bioc = "scRepertoire" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scRepertoire_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scRepertoire/scRepertoire_1.12.0.tar.gz"]

	version("1.12.0", md5="3debd173702ebe6c551ba6c572a76c25")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggalluvial", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-powertcr", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-seuratobject", type=("build", "run"))
