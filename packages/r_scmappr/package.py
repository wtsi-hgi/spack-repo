# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScmappr(RPackage):
	"""Single Cell Mapper

	The single cell mapper (scMappR) R package contains a suite of bioinformatic tools that provide experimentally relevant cell-type specific information to a list of differentially expressed genes (DEG). The function "scMappR_and_pathway_analysis" reranks DEGs to generate cell-type specificity scores called cell-weighted fold-changes. Users input a list of DEGs, normalized counts, and a signature matrix into this function. scMappR then re-weights bulk DEGs by cell-type specific expression from the signature matrix, cell-type proportions from RNA-seq deconvolution and the ratio of cell-type proportions between the two conditions to account for changes in cell-type proportion. With cwFold-changes calculated, scMappR uses two approaches to utilize cwFold-changes to complete cell-type specific pathway analysis. The "process_dgTMatrix_lists" function in the scMappR package contains an automated scRNA-seq processing pipeline where users input scRNA-seq count data, which is made compatible for scMappR and other R packages that analyze scRNA-seq data. We further used this to store hundreds up regularly updating signature matrices. The functions "tissue_by_celltype_enrichment", "tissue_scMappR_internal", and "tissue_scMappR_custom" combine these consistently processed scRNAseq count data with gene-set enrichment tools to allow for cell-type marker enrichment of a generic gene list (e.g. GWAS hits). Reference: Sokolowski,D.J., Faykoo-Martinez,M., Erdman,L., Hou,H., Chan,C., Zhu,H., Holmes,M.M., Goldenberg,A. and Wilson,M.D. (2021) Single-cell mapper (scMappR): using scRNA-seq to infer cell-type specificities of differentially expressed genes. NAR Genomics and Bioinformatics. 3(1). Iqab011. <doi:10.1093/nargab/lqab011>.
	"""
	
	cran = "scMappR" 

	version("1.0.11", md5="e5240532b94e10747551759745abd723")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-gprofiler", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-gprofiler2", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-adapts", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
