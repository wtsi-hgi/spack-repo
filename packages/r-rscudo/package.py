# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRscudo(RPackage):
	"""Signature-based Clustering for Diagnostic Purposes

	SCUDO (Signature-based Clustering for Diagnostic Purposes) is a rank-based method for the analysis of gene expression profiles for diagnostic and classification purposes. It is based on the identification of sample-specific gene signatures composed of the most up- and down-regulated genes for that sample. Starting from gene expression data, functions in this package identify sample-specific gene signatures and use them to build a graph of samples. In this graph samples are joined by edges if they have a similar expression profile, according to a pre-computed similarity matrix. The similarity between the expression profiles of two samples is computed using a method similar to GSEA. The graph of samples can then be used to perform community clustering or to perform supervised classification of samples in a testing set.
	"""
	
	homepage = "https://github.com/Matteo-Ciciani/scudo"
	bioc = "rScudo"

	version("1.24.0", commit="3ea6f0e0e074a9ee3b573ad9d92a125f06699f7c")
	version("1.18.1", commit="e13e994bf7300b2035777ae0a825536c0c42f0a6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
