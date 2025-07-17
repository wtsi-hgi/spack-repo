# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeast(RPackage):
    """FEAture SelcTion (FEAST) for Single-cell clustering

    Cell clustering is one of the most important and commonly performed tasks in single-cell RNA sequencing (scRNA-seq) data analysis. An important step in cell clustering is to select a subset of genes (referred to as “features”), whose expression patterns will then be used for downstream clustering. A good set of features should include the ones that distinguish different cell types, and the quality of such set could have significant impact on the clustering accuracy. FEAST is an R library for selecting most representative features before performing the core of scRNA-seq clustering. It can be used as a plug-in for the etablished clustering algorithms such as SC3, TSCAN, SHARP, SIMLR, and Seurat. The core of FEAST algorithm includes three steps: 1. consensus clustering; 2. gene-level significance inference; 3. validation of an optimized feature set.
    """

    bioc = "FEAST"

    version("1.16.0", commit="29ba93eaee10e67c11a1335680862dcab4d31598")
    version("1.10.0", commit="fe87a45d56261ecce61272ff5196bfb9c3ed9490")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-irlba", type=("build", "run"))
    depends_on("r-tscan", type=("build", "run"))
    depends_on("r-sc3", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
