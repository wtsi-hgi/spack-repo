# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJrsicklsnmf(RPackage):
	"""Multimodal Single-Cell Omics Dimensionality Reduction

	Methods to perform Joint graph Regularized Single-Cell Kullback-Leibler Sparse Non-negative Matrix Factorization ('jrSiCKLSNMF', pronounced "junior sickles NMF") on quality controlled single-cell multimodal omics count data. 'jrSiCKLSNMF' specifically deals with dual-assay scRNA-seq and scATAC-seq data. This package contains functions to extract meaningful latent factors that are shared across omics modalities. These factors enable accurate cell-type clustering and facilitate visualizations. Methods for pre-processing, clustering, and mini-batch updates and other adaptations for larger datasets are also included. For further details on the methods used in this package please see Ellis, Roy, and Datta (2023) <doi:10.3389/fgene.2023.1179439>.
	"""
	
	cran = "jrSiCKLSNMF" 

	version("1.2.1", md5="4e2af8a7838ff3c2ca699a79f05cbedb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-clvalid", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
