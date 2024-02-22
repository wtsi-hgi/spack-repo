# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrigger(RPackage):
	"""Transcriptional Regulatory Inference from Genetics of Gene ExpRession

	This R package provides tools for the statistical analysis of integrative genomic data that involve some combination of: genotypes, high-dimensional intermediate traits (e.g., gene expression, protein abundance), and higher-order traits (phenotypes). The package includes functions to: (1) construct global linkage maps between genetic markers and gene expression; (2) analyze multiple-locus linkage (epistasis) for gene expression; (3) quantify the proportion of genome-wide variation explained by each locus and identify eQTL hotspots; (4) estimate pair-wise causal gene regulatory probabilities and construct gene regulatory networks; and (5) identify causal genes for a quantitative trait of interest.
	"""
	
	bioc = "trigger" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/trigger_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/trigger/trigger_1.48.0.tar.gz"]

	version("1.48.0", md5="d8cb2a76223f510ff08d9dcbf1d6210c")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
