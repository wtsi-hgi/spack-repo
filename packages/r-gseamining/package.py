# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGseamining(RPackage):
	"""Make Biological Sense of Gene Set Enrichment Analysis Outputs

	Gene Set Enrichment Analysis is a very powerful and interesting computational method that allows an easy correlation between differential expressed genes and biological processes. Unfortunately, although it was designed to help researchers to interpret gene expression data it can generate huge amounts of results whose biological meaning can be difficult to interpret. Many available tools rely on the hierarchically structured Gene Ontology (GO) classification to reduce reundandcy in the results. However, due to the popularity of GSEA many more gene set collections, such as those in the Molecular Signatures Database are emerging. Since these collections are not organized as those in GO, their usage for GSEA do not always give a straightforward answer or, in other words, getting all the meaninful information can be challenging with the currently available tools. For these reasons, GSEAmining was born to be an easy tool to create reproducible reports to help researchers make biological sense of GSEA outputs. Given the results of GSEA, GSEAmining clusters the different gene sets collections based on the presence of the same genes in the leadind edge (core) subset. Leading edge subsets are those genes that contribute most to the enrichment score of each collection of genes or gene sets. For this reason, gene sets that participate in similar biological processes should share genes in common and in turn cluster together. After that, GSEAmining is able to identify and represent for each cluster: - The most enriched terms in the names of gene sets (as wordclouds) - The most enriched genes in the leading edge subsets (as bar plots). In each case, positive and negative enrichments are shown in different colors so it is easy to distinguish biological processes or genes that may be of interest in that particular study.
	"""
	
	bioc = "GSEAmining"

	version("1.18.0", commit="f8670310aa6d82b23aa6927a81132cb31d4f9555")
	version("1.12.0", commit="b6a4559dc26144a5f64f34e3b86e6cf8ff9884e3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggwordcloud", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
