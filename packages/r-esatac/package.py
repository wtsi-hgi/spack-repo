# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsatac(RPackage):
	"""An Easy-to-use Systematic pipeline for ATACseq data analysis

	This package provides a framework and complete preset pipeline for quantification and analysis of ATAC-seq Reads. It covers raw sequencing reads preprocessing (FASTQ files), reads alignment (Rbowtie2), aligned reads file operations (SAM, BAM, and BED files), peak calling (F-seq), genome annotations (Motif, GO, SNP analysis) and quality control report. The package is managed by dataflow graph. It is easy for user to pass variables seamlessly between processes and understand the workflow. Users can process FASTQ files through end-to-end preset pipeline which produces a pretty HTML report for quality control and preliminary statistical results, or customize workflow starting from any intermediate stages with esATAC functions easily and flexibly.
	"""
	
	homepage = "https://github.com/wzthu/esATAC"
	bioc = "esATAC"

	version("1.30.0", commit="b2a7f511b6e4f67e1929175498c7e86aed94130e")
	version("1.24.0", commit="fc5274bbd5b2ac96b8edbf4a5070b594acb18fa8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-pipeframe", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rbowtie2", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-chipseeker", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-jaspar2018", type=("build", "run"))
	depends_on("r-tfbstools", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-motifmatchr", type=("build", "run"))
