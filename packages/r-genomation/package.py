# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomation(RPackage):
	"""Summary, annotation and visualization of genomic data

	A package for summary and annotation of genomic intervals. Users can visualize and quantify genomic intervals over pre-defined functional regions, such as promoters, exons, introns, etc. The genomic intervals represent regions with a defined chromosome position, which may be associated with a score, such as aligned reads from HT-seq experiments, TF binding sites, methylation scores, etc. The package can use any tabular genomic feature data as long as it has minimal information on the locations of genomic intervals. In addition, It can use BAM or BigWig files as input.
	"""
	
	homepage = "http://bioinformatics.mdc-berlin.de/genomation/"
	bioc = "genomation" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/genomation_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/genomation/genomation_1.34.0.tar.gz"]

	version("1.34.0", sha256="6c7e40caee1115a28617c2a0a0837c92701dbce7511277c078a5957a50e877ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings@2.47.6:", type=("build", "run"))
	depends_on("r-bsgenome@1.47.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-genomicalignments@1.15.6:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
	depends_on("r-seqpattern", type=("build", "run"))
	depends_on("r-rtracklayer@1.39.7:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
