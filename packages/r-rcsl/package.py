# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcsl(RPackage):
	"""Rank Constrained Similarity Learning for single cell RNA sequencing data

	A novel clustering algorithm and toolkit RCSL (Rank Constrained Similarity Learning) to accurately identify various cell types using scRNA-seq data from a complex tissue. RCSL considers both lo-cal similarity and global similarity among the cells to discern the subtle differences among cells of the same type as well as larger differences among cells of different types. RCSL uses Spearman’s rank correlations of a cell’s expression vector with those of other cells to measure its global similar-ity, and adaptively learns neighbour representation of a cell as its local similarity. The overall similar-ity of a cell to other cells is a linear combination of its global similarity and local similarity.
	"""
	
	homepage = "https://github.com/QinglinMei/RCSL"
	bioc = "RCSL" 

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", commit="ef869351106e5a8df0ea523858c665b1a78674e6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcppannoy", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-nbclust", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
