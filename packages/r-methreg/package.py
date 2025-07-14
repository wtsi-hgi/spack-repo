# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethreg(RPackage):
	"""Assessing the regulatory potential of DNA methylation regions or sites on gene transcription

	Epigenome-wide association studies (EWAS) detects a large number of DNA methylation differences, often hundreds of differentially methylated regions and thousands of CpGs, that are significantly associated with a disease, many are located in non-coding regions. Therefore, there is a critical need to better understand the functional impact of these CpG methylations and to further prioritize the significant changes. MethReg is an R package for integrative modeling of DNA methylation, target gene expression and transcription factor binding sites data, to systematically identify and rank functional CpG methylations. MethReg evaluates, prioritizes and annotates CpG sites with high regulatory potential using matched methylation and gene expression data, along with external TF-target interaction databases based on manually curation, ChIP-seq experiments or gene regulatory network analysis.
	"""
	
	bioc = "MethReg" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MethReg_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MethReg/MethReg_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="56d0158f27fca8c25a26aceeffb3de7ffcdb98aade3ffb8748eee44d5b1114c3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-sesamedata", type=("build", "run"))
	depends_on("r-sesame", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
