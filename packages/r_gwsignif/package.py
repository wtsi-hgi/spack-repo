# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwsignif(RPackage):
	"""Estimating Genome-Wide Significance for Whole Genome Sequencing
Studies, Either Single SNP Tests or Region-Based Tests

	The correlations and linkage disequilibrium between tests can vary as a function of minor allele frequency thresholds used to filter variants, and also varies with different choices of test statistic for region-based tests. Appropriate genome-wide significance thresholds can be estimated empirically through permutation on only a small proportion of the whole genome. 
	"""
	
	cran = "GWsignif" 

	version("1.2", md5="d411cea651ed788f24d1c9f8e71f695a")

