# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcds(RPackage):
	"""Identification of Cancer Dysfunctional Subpathway with Omics
Data

	Identify Cancer Dysfunctional Sub-pathway by integrating gene expression, DNA methylation and copy number variation, and pathway topological information. 1)We firstly calculate the gene risk scores by integrating three kinds of data: DNA methylation, copy number variation, and gene expression.  2)Secondly, we perform a greedy search algorithm to identify the key dysfunctional sub-pathways within the pathways for which the discriminative scores were locally maximal. 3)Finally, the permutation test was used to calculate statistical significance level for these key dysfunctional sub-pathways.
	"""
	
	cran = "ICDS" 

	version("0.1.2", md5="e3b54bd77638cd0b8d889c143233f422")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-graphite", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
