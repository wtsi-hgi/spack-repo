# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHermes(RPackage):
	"""Preprocessing, analyzing, and reporting of RNA-seq data

	Provides classes and functions for quality control, filtering, normalization and differential expression analysis of pre-processed RNA-seq data. Data can be imported from `SummarizedExperiment` as well as `matrix` objects and can be annotated from BioMart. Filtering for genes without too low expression or containing required annotations, as well as filtering for samples with sufficient correlation to other samples or total number of reads is supported. The standard normalization methods including `cpm`, `rpkm` and `tpm` can be used, and `DESeq2` as well as `voom` differential expression analyses are available.
	"""
	
	homepage = "https://github.com/insightsengineering/hermes/"
	bioc = "hermes" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hermes_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hermes/hermes_1.6.0.tar.gz"]

	version("1.6.0", md5="af1e1dd4bab597cfb7b0bd12a1e9e7dd")

	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.16:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel@0.9:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
