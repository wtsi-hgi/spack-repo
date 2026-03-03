# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLncpath(RPackage):
	"""Identifying the Pathways Regulated by LncRNA Sets of Interest

	Identifies pathways synergisticly regulated by the interested lncRNA(long non-coding RNA) sets based on a lncRNA-mRNA(messenger RNA) interaction network. 1) The lncRNA-mRNA interaction network was built from the protein-protein interactions and the lncRNA-mRNA co-expression relationships in 28 RNA-Seq data sets. 2) The interested lncRNAs can be mapped into networks as seed nodes and a random walk strategy will be performed to evaluate the rate of each coding genes influenced by the seed lncRNAs. 3) Pathways regulated by the lncRNA set will be evaluated by a weighted Kolmogorov-Smirnov statistic as an ES Score. 4) The p value and false discovery rate value will also be calculated through a permutation analysis. 5) The running score of each pathway can be plotted and the heat map of each pathway can also be plotted if an expression profile is provided. 6) The rank and scores of the gene list of each pathway can be printed.
	"""
	
	cran = "LncPath" 

	version("1.1", md5="7f1e3ed93e876d106a9b4cec2a236f7e")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
