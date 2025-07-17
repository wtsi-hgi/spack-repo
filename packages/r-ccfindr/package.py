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

    version("1.28.0", commit="9ada3b2d5477549346e3ba7d3436bc9916a66135")
    version("1.22.0", commit="ac6bcb17112b1911edc75328c50fad48a6905447")

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
