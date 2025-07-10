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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rScudo_1.18.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rScudo/rScudo_1.18.1.tar.gz"]

	version("1.18.1", sha256="841088d66fece79c975bae81c109dd68a7e91f58659287db3e9df691f684f398")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
