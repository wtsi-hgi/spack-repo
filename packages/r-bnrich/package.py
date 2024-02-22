# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnrich(RPackage):
	"""Pathway Enrichment Analysis Based on Bayesian Network

	Maleknia et al. (2020) <doi:10.1101/2020.01.13.905448>. A novel pathway enrichment analysis package based on Bayesian network to investigate the topology features of the pathways. firstly, 187 kyoto encyclopedia of genes and genomes (KEGG) human non-metabolic pathways which their cycles were eliminated by biological approach, enter in analysis as Bayesian network structures. The constructed Bayesian network were optimized by the Least Absolute Shrinkage Selector Operator (lasso) and the parameters were learned based on gene expression data. Finally, the impacted pathways were enriched by Fisher’s Exact Test on significant parameters.
	"""
	
	homepage = "https://github.com/Samaneh-Bioinformatics/BNrich"
	cran = "BNrich" 

	version("0.1.1", md5="a422857edca29f4c942bf7d61ce690d1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
