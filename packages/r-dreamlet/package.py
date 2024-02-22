# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDreamlet(RPackage):
	"""Cohort-scale differential expression analysis of single cell data using linear (mixed) models

	Recent advances in single cell/nucleus transcriptomic technology has enabled collection of cohort-scale datasets to study cell type specific gene expression differences associated disease state, stimulus, and genetic regulation. The scale of these data, complex study designs, and low read count per cell mean that characterizing cell type specific molecular mechanisms requires a user-frieldly, purpose-build analytical framework. We have developed the dreamlet package that applies a pseudobulk approach and fits a regression model for each gene and cell cluster to test differential expression across individuals associated with a trait of interest. Use of precision-weighted linear mixed models enables accounting for repeated measures study designs, high dimensional batch effects, and varying sequencing depth or observed cells per biosample.
	"""
	
	homepage = "https://DiseaseNeurogenomics.github.io/dreamlet"
	bioc = "dreamlet" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/dreamlet_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/dreamlet/dreamlet_1.0.0.tar.gz"]

	version("1.0.0", md5="34ea1ec9e44c635699ed9cf8deed29cd")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-variancepartition@1.31.18:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-sparsematrixstats", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-zenith@1.1.2:", type=("build", "run"))
	depends_on("r-mashr@0.2.52:", type=("build", "run"))
	depends_on("r-ashr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-scattermore", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lme4@1.1.33:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
