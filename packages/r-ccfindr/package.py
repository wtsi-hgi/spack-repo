# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcfindr(RPackage):
	"""Cancer Clone Finder

	A collection of tools for cancer genomic data clustering analyses, including those for single cell RNA-seq. Cell clustering and feature gene selection analysis employ Bayesian (and maximum likelihood) non-negative matrix factorization (NMF) algorithm. Input data set consists of RNA count matrix, gene, and cell bar code annotations.  Analysis outputs are factor matrices for multiple ranks and marginal likelihood values for each rank. The package includes utilities for downstream analyses, including meta-gene identification, visualization, and construction of rank-based trees for clusters.
	"""
	
	homepage = "http://dx.doi.org/10.26508/lsa.201900443"
	bioc = "ccfindR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ccfindR_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ccfindR/ccfindR_1.22.0.tar.gz"]

	version("1.22.0", md5="0a0dd7c35273c39673f992bed7fa952d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rmpi", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
