# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglecellhaystack(RPackage):
	"""A Universal Differential Expression Prediction Tool for
Single-Cell and Spatial Genomics Data

	One key exploratory analysis step in single-cell genomics data analysis
    is the prediction of features with different activity levels. For example, we want 
    to predict differentially expressed genes (DEGs) in single-cell RNA-seq data, 
    spatial DEGs in spatial transcriptomics data, or differentially accessible 
    regions (DARs) in single-cell ATAC-seq data. 'singleCellHaystack' predicts differentially
    active features in single cell omics datasets without relying on the clustering
    of cells into arbitrary clusters. 'singleCellHaystack' uses Kullback-Leibler 
    divergence to find features (e.g., genes, genomic regions, etc) that are active
    in subsets of cells that are non-randomly positioned inside an input space (such as 
    1D trajectories, 2D tissue sections, multi-dimensional embeddings, etc). For 
    the theoretical background of 'singleCellHaystack' we refer to our original paper
    Vandenbon and Diez (Nature Communications, 2020) <doi:10.1038/s41467-020-17900-3>
    and our update Vandenbon and Diez (Scientific Reports, 2023) <doi:10.1038/s41598-023-38965-2>.
	"""
	
	homepage = "https://alexisvdb.github.io/singleCellHaystack/"
	cran = "singleCellHaystack" 

	version("1.0.2", md5="74aff38c8e2dbea3f9828557fc748b0d")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
