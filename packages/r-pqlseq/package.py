# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPqlseq(RPackage):
	"""Efficient Mixed Model Analysis of Count Data in Large-Scale
Genomic Sequencing Studies

	An efficient tool designed for differential analysis of large-scale RNA sequencing (RNAseq) data and Bisulfite sequencing (BSseq) data in the presence of individual relatedness and population structure. 'PQLseq' first fits a Generalized Linear Mixed Model (GLMM) with adjusted covariates, predictor of interest and random effects to account for population structure and individual relatedness, and then performs Wald tests for each gene in RNAseq or site in BSseq. 
	"""
	
	cran = "PQLseq" 

	version("1.2.1", md5="6244e739f72e7d42895d74de7c35fcb9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
