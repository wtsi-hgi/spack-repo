# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScgate(RPackage):
	"""Marker-Based Cell Type Purification for Single-Cell Sequencing
Data

	A common bioinformatics task in single-cell data analysis is to purify a cell type or cell population of interest from heterogeneous datasets. 'scGate' automatizes marker-based purification of specific cell populations, without requiring training data or reference gene expression profiles. Briefly, 'scGate' takes as input: i) a gene expression matrix stored in a 'Seurat' object and ii) a “gating model” (GM), consisting of a set of marker genes that define the cell population of interest. The GM can be as simple as a single marker gene, or a combination of positive and negative markers. More complex GMs can be constructed in a hierarchical fashion, akin to gating strategies employed in flow cytometry. 'scGate' evaluates the strength of signature marker expression in each cell using the rank-based method 'UCell', and then performs k-nearest neighbor (kNN) smoothing by calculating the mean 'UCell' score across neighboring cells. kNN-smoothing aims at compensating for the large degree of sparsity in scRNA-seq data. Finally, a universal threshold over kNN-smoothed signature scores is applied in binary decision trees generated from the user-provided gating model, to annotate cells as either “pure” or “impure”, with respect to the cell population of interest. See the related publication Andreatta et al. (2022) <doi:10.1093/bioinformatics/btac141>.
	"""
	
	homepage = "https://github.com/carmonalab/scGate"
	cran = "scGate" 

	version("1.6.0", md5="61cf22060ac64473db8a345bf391d6e2")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-seurat@4:", type=("build", "run"))
	depends_on("r-ucell@2.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
