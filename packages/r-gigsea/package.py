# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGigsea(RPackage):
	"""Genotype Imputed Gene Set Enrichment Analysis

	We presented the Genotype-imputed Gene Set Enrichment Analysis (GIGSEA), a novel method that uses GWAS-and-eQTL-imputed trait-associated differential gene expression to interrogate gene set enrichment for the trait-associated SNPs. By incorporating eQTL from large gene expression studies, e.g. GTEx, GIGSEA appropriately addresses such challenges for SNP enrichment as gene size, gene boundary, SNP distal regulation, and multiple-marker regulation. The weighted linear regression model, taking as weights both imputation accuracy and model completeness, was used to perform the enrichment test, properly adjusting the bias due to redundancy in different gene sets. The permutation test, furthermore, is used to evaluate the significance of enrichment, whose efficiency can be largely elevated by expressing the computational intensive part in terms of large matrix operation. We have shown the appropriate type I error rates for GIGSEA (<5%), and the preliminary results also demonstrate its good performance to uncover the real signal.
	"""
	
	bioc = "GIGSEA"

	version("1.26.0", commit="4ba260c93c171e546f11abf368097e39181761dc")
	version("1.20.0", commit="bed750298de97f680393f45eaa93c1787810eecd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-locfdr", type=("build", "run"))
