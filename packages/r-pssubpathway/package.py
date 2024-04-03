# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPssubpathway(RPackage):
	"""Flexible Identification of Phenotype-Specific Subpathways

	A network-based systems biology tool for flexible identification of phenotype-specific subpathways in the cancer gene expression data 
  with multiple categories (such as multiple subtype or developmental stages of cancer). Subtype Set Enrichment Analysis (SubSEA) and Dynamic Changed 
  Subpathway Analysis (DCSA) are developed to flexible identify subtype specific and dynamic changed subpathways respectively. The operation modes 
  include extraction of subpathways from biological pathways, inference of subpathway activities in the context of gene expression data, identification 
  of subtype specific subpathways with SubSEA, identification of dynamic changed subpathways associated with the cancer developmental stage with DCSA, 
  and visualization of the activities of resulting subpathways by using box plots and heat maps. Its capabilities render the tool could find the specific
  abnormal subpathways in the cancer dataset with multi-phenotype samples.
	"""
	
	cran = "psSubpathway" 

	version("0.1.3", md5="6f3b002db599ad063b4b3a1f1ea7c6cb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mpmi", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
