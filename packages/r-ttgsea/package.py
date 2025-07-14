# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtgsea(RPackage):
	"""Tokenizing Text of Gene Set Enrichment Analysis

	Functional enrichment analysis methods such as gene set enrichment analysis (GSEA) have been widely used for analyzing gene expression data. GSEA is a powerful method to infer results of gene expression data at a level of gene sets by calculating enrichment scores for predefined sets of genes. GSEA depends on the availability and accuracy of gene sets. There are overlaps between terms of gene sets or categories because multiple terms may exist for a single biological process, and it can thus lead to redundancy within enriched terms. In other words, the sets of related terms are overlapping. Using deep learning, this pakage is aimed to predict enrichment scores for unique tokens or words from text in names of gene sets to resolve this overlapping set issue. Furthermore, we can coin a new term by combining tokens and find its enrichment score by predicting such a combined tokens.
	"""
	
	bioc = "ttgsea" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ttgsea_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ttgsea/ttgsea_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="3cee0ee4e930eb2fce6557723fbb2ac30a40589b80aa3174004d2a372108d303")

	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-text2vec", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
	depends_on("r-textstem", type=("build", "run"))
	depends_on("r-stopwords", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
