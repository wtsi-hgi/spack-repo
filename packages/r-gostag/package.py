# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGostag(RPackage):
	"""A tool to use GO Subtrees to Tag and Annotate Genes within a set

	Gene lists derived from the results of genomic analyses are rich in biological information. For instance, differentially expressed genes (DEGs) from a microarray or RNA-Seq analysis are related functionally in terms of their response to a treatment or condition. Gene lists can vary in size, up to several thousand genes, depending on the robustness of the perturbations or how widely different the conditions are biologically. Having a way to associate biological relatedness between hundreds and thousands of genes systematically is impractical by manually curating the annotation and function of each gene. Over-representation analysis (ORA) of genes was developed to identify biological themes. Given a Gene Ontology (GO) and an annotation of genes that indicate the categories each one fits into, significance of the over-representation of the genes within the ontological categories is determined by a Fisher's exact test or modeling according to a hypergeometric distribution. Comparing a small number of enriched biological categories for a few samples is manageable using Venn diagrams or other means for assessing overlaps. However, with hundreds of enriched categories and many samples, the comparisons are laborious. Furthermore, if there are enriched categories that are shared between samples, trying to represent a common theme across them is highly subjective. goSTAG uses GO subtrees to tag and annotate genes within a set. goSTAG visualizes the similarities between the over-representation of DEGs by clustering the p-values from the enrichment statistical tests and labels clusters with the GO term that has the most paths to the root within the subtree generated from all the GO terms in the cluster.
	"""
	
	bioc = "goSTAG" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/goSTAG_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/goSTAG/goSTAG_1.26.0.tar.gz"]

	version("1.26.0", md5="8d3245abbcc5813366a9393dc7bf79c7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
