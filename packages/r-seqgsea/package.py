# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqgsea(RPackage):
	"""Gene Set Enrichment Analysis (GSEA) of RNA-Seq Data: integrating differential expression and splicing

	The package generally provides methods for gene set enrichment analysis of high-throughput RNA-Seq data by integrating differential expression and splicing. It uses negative binomial distribution to model read count data, which accounts for sequencing biases and biological variation. Based on permutation tests, statistical significance can also be achieved regarding each gene's differential expression and splicing, respectively.
	"""
	
	bioc = "SeqGSEA"

	version("1.48.0", commit="ea0980af7ad1b8e7f44a54563e4e025e5c7c641b")
	version("1.42.0", commit="09222b3729f2d052c7dc6980e08845fcb631c08d")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
