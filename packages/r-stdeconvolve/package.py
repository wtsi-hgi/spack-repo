# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStdeconvolve(RPackage):
	"""Reference-free Cell-Type Deconvolution of Multi-Cellular Spatially Resolved Transcriptomics Data

	STdeconvolve as an unsupervised, reference-free approach to infer latent cell-type proportions and transcriptional profiles within multi-cellular spatially-resolved pixels from spatial transcriptomics (ST) datasets. STdeconvolve builds on latent Dirichlet allocation (LDA), a generative statistical model commonly used in natural language processing for discovering latent topics in collections of documents. In the context of natural language processing, given a count matrix of words in documents, LDA infers the distribution of words for each topic and the distribution of topics in each document. In the context of ST data, given a count matrix of gene expression in multi-cellular ST pixels, STdeconvolve applies LDA to infer the putative transcriptional profile for each cell-type and the proportional representation of each cell-type in each multi-cellular ST pixel.
	"""
	
	homepage = "https://jef.works/STdeconvolve/"
	bioc = "STdeconvolve" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/STdeconvolve_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/STdeconvolve/STdeconvolve_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="172c5e0ed57d279eaebc7496e7be51af4d460aa2902495abbc5a6aee91077c9b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scatterpie", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-liger", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
