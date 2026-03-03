# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmmixgene(RPackage):
	"""A Mixture Model-Based Approach to the Clustering of Microarray
Expression Data

	Provides unsupervised selection and clustering of microarray data
    using mixture models. Following the methods described in McLachlan, Bean and
    Peel (2002) <doi:10.1093/bioinformatics/18.3.413> a subset of genes are selected
    based one the likelihood ratio statistic for the test of one versus two
    components when fitting mixtures of t-distributions to the expression data
    for each gene. The dimensionality of this gene subset is further reduced through
    the use of mixtures of factor analyzers, allowing the tissue samples to be
    clustered by fitting mixtures of normal distributions.
	"""
	
	cran = "EMMIXgene" 

	version("0.1.4", md5="a5e3a0face05301737a53a4ddc509dfa")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
