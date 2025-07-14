# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpimix(RPackage):
	"""EpiMix: an integrative tool for the population-level analysis of DNA methylation

	EpiMix is a comprehensive tool for the integrative analysis of high-throughput DNA methylation data and gene expression data. EpiMix enables automated data downloading (from TCGA or GEO), preprocessing, methylation modeling, interactive visualization and functional annotation.To identify hypo- or hypermethylated CpG sites across physiological or pathological conditions, EpiMix uses a beta mixture modeling to identify the methylation states of each CpG probe and compares the methylation of the experimental group to the control group.The output from EpiMix is the functional DNA methylation that is predictive of gene expression. EpiMix incorporates specialized algorithms to identify functional DNA methylation at various genetic elements, including proximal cis-regulatory elements of protein-coding genes, distal enhancers, and genes encoding microRNAs and lncRNAs.
	"""
	
	bioc = "EpiMix"

	version("1.10.0", commit="d6d994dc4498164815553ef33acdb18ef29586b2")
	version("1.4.0", commit="dd3578df09afa15cd05e3d90b66545e8daf84898")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-epimix-data@1.2.2:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-elmer-data", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rpmm", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
