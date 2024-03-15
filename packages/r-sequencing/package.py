# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSequencing(RPackage):
	"""Introduction to Bioconductor for Sequence Data

	Bioconductor enables the analysis and comprehension of high- throughput genomic data. We have a vast number of packages that allow rigorous statistical analysis of large data while keeping technological artifacts in mind. Bioconductor helps users place their analytic results into biological context, with rich opportunities for visualization. Reproducibility is an important goal in Bioconductor analyses. Different types of analysis can be carried out using Bioconductor, for example; Sequencing : RNASeq, ChIPSeq, variants, copy number etc.; Microarrays: expression, SNP, etc.; Domain specific analysis : Flow cytometry, Proteomics etc. For these analyses, one typically imports and works with diverse sequence-related file types, including fasta, fastq, BAM, gtf, bed, and wig files, among others. Bioconductor packages support import, common and advanced sequence manipulation operations such as trimming, transformation, and alignment including quality assessment.
	"""
	
	homepage = "https://www.bioconductor.org/help/workflows/sequencing/"
	bioc = "sequencing" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/sequencing_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/sequencing/sequencing_1.26.0.tar.gz"]

	version("1.26.0", md5="bfc08d88720839f3233d2457b3b88a8c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-rnaseqdata-hnrnpc-bam-chr14", type=("build", "run"))

	# workflow