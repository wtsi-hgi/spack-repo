# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorto(RPackage):
	"""Inference of Gene Regulatory Networks

	We present 'corto' (Correlation Tool), a simple package to infer
 gene regulatory networks and visualize master regulators from gene expression
 data using DPI (Data Processing Inequality) and bootstrapping to recover edges.
 An initial step is performed to calculate all significant
 edges between a list of source nodes (centroids) and target genes.
 Then all triplets containing two centroids and one target are tested
 in a DPI step which removes edges. A bootstrapping process then calculates
 the robustness of the network, eventually re-adding edges previously removed by DPI.
 The algorithm has been optimized to run outside a computing cluster, using a fast correlation
 implementation. The package finally provides functions to calculate network enrichment
 analysis from RNA-Seq and ATAC-Seq signatures as described in the article by
 Giorgi lab (2020) <doi:10.1093/bioinformatics/btaa223>.
	"""
	
	cran = "corto" 

	version("1.2.4", md5="de011d8c4621997d277115fba4515eb4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
