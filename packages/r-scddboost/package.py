# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScddboost(RPackage):
	"""A compositional model to assess expression changes from single-cell rna-seq data

	scDDboost is an R package to analyze changes in the distribution of single-cell expression data between two experimental conditions. Compared to other methods that assess differential expression, scDDboost benefits uniquely from information conveyed by the clustering of cells into cellular subtypes. Through a novel empirical Bayesian formulation it calculates gene-specific posterior probabilities that the marginal expression distribution is the same (or different) between the two conditions. The implementation in scDDboost treats gene-level expression data within each condition as a mixture of negative binomial distributions.
	"""
	
	homepage = "https://github.com/wiscstatman/scDDboost"
	bioc = "scDDboost" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scDDboost_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scDDboost/scDDboost_1.4.0.tar.gz"]

	version("1.4.0", md5="ac0cac5975ebe4025ea07ad00e132847")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-ebseq", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-oscope", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
