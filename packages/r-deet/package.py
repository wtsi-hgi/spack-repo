# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeet(RPackage):
	"""Differential Expression Enrichment Tool

	Abstract of Manuscript. Differential gene expression analysis using RNA sequencing (RNA-seq) data is a standard approach for making biological discoveries. Ongoing large-scale efforts to process and normalize publicly available gene expression data enable rapid and systematic reanalysis. While several powerful tools systematically process RNA-seq data, enabling their reanalysis, few resources systematically recompute differentially expressed genes (DEGs) generated from individual studies. We developed a robust differential expression analysis pipeline to recompute 3162 human DEG lists from The Cancer Genome Atlas, Genotype-Tissue Expression Consortium, and 142 studies within the Sequence Read Archive. After measuring the accuracy of the recomputed DEG lists, we built the Differential Expression Enrichment Tool (DEET), which enables users to interact with the recomputed DEG lists. DEET, available through CRAN and RShiny, systematically queries which of the recomputed DEG lists share similar genes, pathways, and TF targets to their own gene lists. DEET identifies relevant studies based on shared results with the user’s gene lists, aiding in hypothesis generation and data-driven literature review. Sokolowski, Dustin J., et al. "Differential Expression Enrichment Tool (DEET): an interactive atlas of human differential gene expression." Nucleic Acids Research Genomics and Bioinformatics (2023).
	"""
	
	cran = "DEET" 

	version("1.0.11", md5="946edea29233b20d32df2f6ff3758e25")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-activepathways", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
