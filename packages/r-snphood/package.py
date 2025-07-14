# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnphood(RPackage):
	"""SNPhood: Investigate, quantify and visualise the epigenomic neighbourhood of SNPs using NGS data

	To date, thousands of single nucleotide polymorphisms (SNPs) have been found to be associated with complex traits and diseases. However, the vast majority of these disease-associated SNPs lie in the non-coding part of the genome, and are likely to affect regulatory elements, such as enhancers and promoters, rather than function of a protein. Thus, to understand the molecular mechanisms underlying genetic traits and diseases, it becomes increasingly important to study the effect of a SNP on nearby molecular traits such as chromatin environment or transcription factor (TF) binding. Towards this aim, we developed SNPhood, a user-friendly *Bioconductor* R package to investigate and visualize the local neighborhood of a set of SNPs of interest for NGS data such as chromatin marks or transcription factor binding sites from ChIP-Seq or RNA- Seq experiments. SNPhood comprises a set of easy-to-use functions to extract, normalize and summarize reads for a genomic region, perform various data quality checks, normalize read counts using additional input files, and to cluster and visualize the regions according to the binding pattern. The regions around each SNP can be binned in a user-defined fashion to allow for analysis of very broad patterns as well as a detailed investigation of specific binding shapes. Furthermore, SNPhood supports the integration with genotype information to investigate and visualize genotype-specific binding patterns. Finally, SNPhood can be employed for determining, investigating, and visualizing allele-specific binding patterns around the SNPs of interest.
	"""
	
	homepage = "https://bioconductor.org/packages/SNPhood"
	bioc = "SNPhood" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SNPhood_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SNPhood/SNPhood_1.32.0.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="2eee4411ed434618d8d072ced9f0aec347c158ababba6ff4d825c805441cc729")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-genomeinfodb@1.34.8:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
