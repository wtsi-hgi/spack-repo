# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeq2pathway(RPackage):
	"""a novel tool for functional gene-set (or termed as pathway) analysis of next-generation sequencing data

	Seq2pathway is a novel tool for functional gene-set (or termed as pathway) analysis of next-generation sequencing data, consisting of "seq2gene" and "gene2path" components. The seq2gene links sequence-level measurements of genomic regions (including SNPs or point mutation coordinates) to gene-level scores, and the gene2pathway summarizes gene scores to pathway-scores for each sample. The seq2gene has the feasibility to assign both coding and non-exon regions to a broader range of neighboring genes than only the nearest one, thus facilitating the study of functional non-coding regions. The gene2pathway takes into account the quantity of significance for gene members within a pathway compared those outside a pathway. The output of seq2pathway is a general structure of quantitative pathway-level scores, thus allowing one to functional interpret such datasets as RNA-seq, ChIP-seq, GWAS, and derived from other next generational sequencing experiments.
	"""
	
	bioc = "seq2pathway" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/seq2pathway_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/seq2pathway/seq2pathway_1.34.0.tar.gz"]

	version("1.34.0", md5="4aaa34232c40fdc31f493d67c72742c4")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-gsa", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-seq2pathway-data", type=("build", "run"))
