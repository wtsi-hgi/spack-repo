# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlatypus(RPackage):
	"""Single-Cell Immune Repertoire and Gene Expression Analysis

	We present 'Platypus', an open-source software platform providing a user-friendly interface to investigate B-cell receptor and T-cell receptor repertoires from scSeq experiments. 'Platypus' provides a framework to automate and ease the analysis of single-cell immune repertoires while also incorporating transcriptional information involving unsupervised clustering, gene expression and gene ontology. This R version of 'Platypus' is part of the 'ePlatypus' ecosystem for computational analysis of immunogenomics data: Yermanos et al. (2021) <doi:10.1093/nargab/lqab023>, Cotet et al. (2023) <doi:10.1093/bioinformatics/btad553>.
	"""
	
	cran = "Platypus" 

	version("3.5.0", md5="005c556813774954aaf95b5fda57e6d8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix@1.3.3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-seuratobject@4.1.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-useful", type=("build", "run"))
