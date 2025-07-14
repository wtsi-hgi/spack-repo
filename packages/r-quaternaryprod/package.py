# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuaternaryprod(RPackage):
	"""Computes the Quaternary Dot Product Scoring Statistic for Signed and Unsigned Causal Graphs

	QuaternaryProd is an R package that performs causal reasoning on biological networks, including publicly available networks such as STRINGdb. QuaternaryProd is an open-source alternative to commercial products such as Inginuity Pathway Analysis. For a given a set of differentially expressed genes, QuaternaryProd computes the significance of upstream regulators in the network by performing causal reasoning using the Quaternary Dot Product Scoring Statistic (Quaternary Statistic), Ternary Dot product Scoring Statistic (Ternary Statistic) and Fisher's exact test (Enrichment test). The Quaternary Statistic handles signed, unsigned and ambiguous edges in the network. Ambiguity arises when the direction of causality is unknown, or when the source node (e.g., a protein) has edges with conflicting signs for the same target gene. On the other hand, the Ternary Statistic provides causal reasoning using the signed and unambiguous edges only. The Vignette provides more details on the Quaternary Statistic and illustrates an example of how to perform causal reasoning using STRINGdb.
	"""
	
	bioc = "QuaternaryProd"

	version("1.42.0", commit="5c09d42f0cf81474a0417a0c8a8305dd910d03b2")
	version("1.36.0", commit="ca0cca6bf6ec477bd1121fcf60c2e2447137290f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-yaml@2.1.18:", type=("build", "run"))
