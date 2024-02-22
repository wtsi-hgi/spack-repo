# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigner(RPackage):
	"""Empirical Bayesian approach to mutational signature discovery

	The signeR package provides an empirical Bayesian approach to mutational signature discovery. It is designed to analyze single nucleotide variation (SNV) counts in cancer genomes, but can also be applied to other features as well. Functionalities to characterize signatures or genome samples according to exposure patterns are also provided.
	"""
	
	homepage = "https://github.com/TojalLab/signeR"
	bioc = "signeR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/signeR_2.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/signeR/signeR_2.4.0.tar.gz"]

	version("2.4.0", md5="36ca120021611cebddf20efa74c6bbf7")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-pmcmrplus", type=("build", "run"))
	depends_on("r-pvclust", type=("build", "run"))
	depends_on("r-ppclust", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-maxstat", type=("build", "run"))
	depends_on("r-survivalanalysis", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ada", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-listenv", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-bsplus", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.100:", type=("build", "run"))
