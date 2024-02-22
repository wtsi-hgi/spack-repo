# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeritseq(RPackage):
	"""Heritability of Gene Expression for Next-Generation Sequencing

	Statistical framework to analyze heritability of gene expression 
    based on next-generation sequencing data and simulating sequencing reads. 
    Variance partition coefficients (VPC) are computed using linear mixed effects 
    and generalized linear mixed effects models. Compound Poisson and negative 
    binomial models are included. Reference: Rudra, Pratyaydipta, et al. "Model based heritability scores for high-throughput sequencing data." BMC bioinformatics 18.1 (2017): 143.
	"""
	
	cran = "HeritSeq" 

	version("1.0.2", md5="9b5e951bc341b9186ecb02cfc0a47a8d")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-cplm", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-tweedie", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
