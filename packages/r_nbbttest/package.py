# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbbttest(RPackage):
	"""Negative Binomial Beta t-Test

	We constructed 'NBBttest' for identifying genes or RNA isoforms differentially expressed between two conditions on RNA-seq count data. Package 'NBBttest' can  perform data quality check, data normalization, differential analysis, annotation and graphic analysis. In differential analysis, 'NBBttest' can identify differentially expressed genes and differential RNA isoforms in alternative splicing sites and alternative polyadenylation sites, differential sgRNA, and differential CRISPR (clustered regularly interspaced short palindromic repeats) screening genes. In graphic analysis, 'NBBttest' provides two types of heatmaps to visualize differential expression at gene or isoform level using z-score and n-score and creates pathway heatmap. 'NBBttest' can plot differentially expressed exons within a specified gene. In addition, 'NBBttest' provides a tool for annotation of genes and exons. The methods used in 'NBBttest' were new statistical methods developed from Tan and others (2015) <doi:10.1371/journal.pone.0123658>. The statistical methods are robust and very powerful in identifying genes or RNA isoforms differentially expressed between two conditions in small samples.
	"""
	
	cran = "NBBttest" 

	version("1.0.1", md5="490160eeec2a6fa47958e794e86efaa3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
