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

	version("1.12.0", commit="ae34af0cf73d5fa3c6ae20536d66ce59cee1f2fc")
	version("1.6.0", commit="9cc625d4202755387ee6c851e689f0d868c4bce7")

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
