# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffenrich(RPackage):
	"""Given a List of Gene Symbols, Performs Differential Enrichment
Analysis

	Compare functional enrichment between two experimentally-derived groups of genes or proteins (Peterson, DR., et al.(2018)) <doi: 10.1371/journal.pone.0198139>. Given a list of gene symbols, 'diffEnrich'  will
  perform differential enrichment analysis using the Kyoto Encyclopedia of Genes
  and Genomes (KEGG) REST API. This package provides a number of functions that are 
  intended to be used in a pipeline. Briefly, the user provides a KEGG formatted species id for either human, mouse or rat, and the package will
  download and clean species specific ENTREZ gene IDs and map them to their respective
  KEGG pathways by accessing KEGG's REST API. KEGG's API is used to guarantee the most up-to-date pathway data from KEGG. Next, the user will identify significantly
  enriched pathways from two gene sets, and finally, the user will identify 
  pathways that are differentially enriched between the two gene sets. In addition to 
  the analysis pipeline, this package also provides a plotting function. 
	"""
	
	homepage = "https://github.com/SabaLab/diffEnrich"
	cran = "diffEnrich" 

	version("0.1.2", md5="c1157a279feee496eb6190275d0cfd4f")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
