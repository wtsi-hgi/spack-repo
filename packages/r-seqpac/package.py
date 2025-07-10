# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqpac(RPackage):
	"""Seqpac: A Framework for smallRNA analysis in R using Sequence-Based Counts

	Seqpac provides functions and workflows for analysis of short sequenced reads. It was originally developed for small RNA analysis, but can be implemented on any sequencing raw data (provided as a fastq-file), where the unit of measurement is counts of unique sequences. The core of the seqpac workflow is the generation and subsequence analysis/visualization of a standardized object called PAC. Using an innovative targeting system, Seqpac process, analyze and visualize sample or sequence group differences using the PAC object. A PAC object in its most basic form is a list containing three types of data frames. - Phenotype table (P): Sample names (rows) with associated metadata (columns) e.g. treatment. - Annotation table (A): Unique sequences (rows) with annotation (columns), eg. reference alignments. - Counts table (C): Counts of unique sequences (rows) for each sample (columns). The PAC-object follows the rule: - Row names in P must be identical with column names in C. - Row names in A must be identical with row names in C. Thus P and A describes the columns and rows in C, respectively. The targeting system, will either target specific samples in P (pheno_target) or sequences in A (anno_target) and group them according to a target column in P and A, respectively (see vignettes for more details).
	"""
	
	homepage = "https://github.com/Danis102/seqpac"
	bioc = "seqpac" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/seqpac_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/seqpac/seqpac_1.2.0.tar.gz"]

	version("1.2.0", sha256="c4618b8fdbbd888fca08aa3c1cf3e2d9d56802ac584b654a8bb5e7fd4a9b30e8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biostrings@2.46:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-genomicranges@1.30.3:", type=("build", "run"))
	depends_on("r-rbowtie@1.18:", type=("build", "run"))
	depends_on("r-shortread@1.36.1:", type=("build", "run"))
	depends_on("r-tibble@3.1.2:", type=("build", "run"))
	depends_on("r-biocparallel@1.12:", type=("build", "run"))
	depends_on("r-cowplot@0.9.4:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-digest@0.6.27:", type=("build", "run"))
	depends_on("r-doparallel@1.0.16:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-factoextra@1.0.7:", type=("build", "run"))
	depends_on("r-factominer@1.41:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-iranges@2.12:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-rtracklayer@1.38.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

