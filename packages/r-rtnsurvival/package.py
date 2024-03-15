# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtnsurvival(RPackage):
	"""Survival analysis using transcriptional networks inferred by the RTN package

	RTNsurvival is a tool for integrating regulons generated by the RTN package with survival information. For a given regulon, the 2-tailed GSEA approach computes a differential Enrichment Score (dES) for each individual sample, and the dES distribution of all samples is then used to assess the survival statistics for the cohort. There are two main survival analysis workflows: a Cox Proportional Hazards approach used to model regulons as predictors of survival time, and a Kaplan-Meier analysis assessing the stratification of a cohort based on the regulon activity. All plots can be fine-tuned to the user's specifications.
	"""
	
	bioc = "RTNsurvival" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RTNsurvival_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RTNsurvival/RTNsurvival_1.26.0.tar.gz"]

	version("1.26.0", md5="db9d03eee81fed17fae3acb66a07893f")

	depends_on("r@3.6.3:", type=("build", "run"))
	depends_on("r-rtn@2.14.1:", type=("build", "run"))
	depends_on("r-rtnduals@1.14.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-dunn-test", type=("build", "run"))
