# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellscape(RPackage):
	"""Explores single cell copy number profiles in the context of a single cell tree

	CellScape facilitates interactive browsing of single cell clonal evolution datasets. The tool requires two main inputs: (i) the genomic content of each single cell in the form of either copy number segments or targeted mutation values, and (ii) a single cell phylogeny. Phylogenetic formats can vary from dendrogram-like phylogenies with leaf nodes to evolutionary model-derived phylogenies with observed or latent internal nodes. The CellScape phylogeny is flexibly input as a table of source-target edges to support arbitrary representations, where each node may or may not have associated genomic data. The output of CellScape is an interactive interface displaying a single cell phylogeny and a cell-by-locus genomic heatmap representing the mutation status in each cell for each locus.
	"""
	
	bioc = "cellscape" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cellscape_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cellscape/cellscape_1.26.0.tar.gz"]

	version("1.26.0", md5="869f8784828e9550fc85b302037bf7bf")
	version("1.26.0", commit="ee36e5b05c91739b37585d71ae256206abc9e70a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.5:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.19:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
