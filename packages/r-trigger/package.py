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

	version("1.54.0", commit="c93275c3b4687f78f5c19a2a92a42fe8e18ce9bb")
	version("1.48.0", commit="2656177c4c36a4a7563a1c0beef360501fa0e207")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
