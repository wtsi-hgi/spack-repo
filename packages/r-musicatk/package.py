# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMusicatk(RPackage):
	"""Mutational Signature Comprehensive Analysis Toolkit

	Mutational signatures are carcinogenic exposures or aberrant cellular processes that can cause alterations to the genome. We created musicatk (MUtational SIgnature Comprehensive Analysis ToolKit) to address shortcomings in versatility and ease of use in other pre-existing computational tools. Although many different types of mutational data have been generated, current software packages do not have a flexible framework to allow users to mix and match different types of mutations in the mutational signature inference process. Musicatk enables users to count and combine multiple mutation types, including SBS, DBS, and indels. Musicatk calculates replication strand, transcription strand and combinations of these features along with discovery from unique and proprietary genomic feature associated with any mutation type. Musicatk also implements several methods for discovery of new signatures as well as methods to infer exposure given an existing set of signatures. Musicatk provides functions for visualization and downstream exploratory analysis including the ability to compare signatures between cohorts and find matching signatures in COSMIC V2 or COSMIC V3.
	"""
	
	bioc = "musicatk" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/musicatk_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/musicatk/musicatk_1.12.0.tar.gz"]

	version("1.12.0", md5="50869915aff9dd79823e05b4ae163bc6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mcmcprecision", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixtests", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg38", type=("build", "run"))
	depends_on("r-bsgenome-mmusculus-ucsc-mm9", type=("build", "run"))
	depends_on("r-bsgenome-mmusculus-ucsc-mm10", type=("build", "run"))
	depends_on("r-deconstructsigs", type=("build", "run"))
	depends_on("r-decomptumor2sig", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-philentropy", type=("build", "run"))
	depends_on("r-maftools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
