# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKogmwu(RPackage):
	"""Functional Summary and Meta-Analysis of Gene Expression Data

	Rank-based tests for enrichment of KOG (euKaryotic Orthologous Groups) classes with up- or down-regulated genes based on a continuous measure. The meta-analysis is based on correlation of KOG delta-ranks across datasets (delta-rank is the difference between mean rank of genes belonging to a KOG class and mean rank of all other genes). With binary measure (1 or 0 to indicate significant and non-significant genes), one-tailed Fisher's exact test for over-representation of each KOG class among significant genes will be performed. 
	"""
	
	cran = "KOGMWU" 

	version("1.2", md5="7ba22ab0c9a22685b55ced90564fe5a0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
