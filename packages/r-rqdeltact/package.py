# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqdeltact(RPackage):
	"""Relative Quantification of Gene Expression using Delta Ct
Methods

	The commonly used methods for relative quantification of gene expression are the delta Ct family methods (encompassing 2^-Ct, 2^-dCt, and 2^-ddCt methods), originally proposed by Kenneth J. Livak and Thomas D. Schmittgen (2001) <doi:10.1006/meth.2001.1262>. These methods were designed to analyse gene expression data (Ct values) obtained from qPCR (quantitative Polymerase Chain Reaction) experiments. The main idea is to normalise gene expression values using endogenous control gene, present gene expression levels in linear form by using the 2^-(value)^ transformation, and calculate differences in gene expression levels between groups of samples (or technical replicates of a single sample). The 'RQdeltaCT' package offers functions that encompass all of these steps for comparison of either independent groups of samples or groups with paired samples, together with importing qPCR datasets, performing multi-step quality control of data, enabling numerous data visualisations, enrichment of the standard workflow with additional useful analyses (correlation analysis, Receiver Operating Characteristic analysis, logistic regression), and conveniently export obtained results in table and image formats. The package has been designed to be friendly to non-experts in R programming users.
	"""
	
	homepage = "<https://github.com/Donadelnal/RQdeltaCT>"
	cran = "RQdeltaCT" 

	version("1.2.1", md5="6149fcb66e612011146ded0327885bc7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-ctrlgene", type=("build", "run"))
	depends_on("r-ggsignif", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-oddsratio", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
