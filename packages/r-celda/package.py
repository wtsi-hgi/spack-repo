# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelda(RPackage):
    """CEllular Latent Dirichlet Allocation

    Celda is a suite of Bayesian hierarchical models for clustering single-cell RNA-sequencing (scRNA-seq) data. It is able to perform "bi-clustering" and simultaneously cluster genes into gene modules and cells into cell subpopulations. It also contains DecontX, a novel Bayesian method to computationally estimate and remove RNA contamination in individual cells without empty droplet information. A variety of scRNA-seq data visualization functions is also included.
    """

    bioc = "celda"

    version("1.24.0", commit="141d97696c69861c8ad6d0e7934172e40a2a3b7b")
    version("1.18.1", md5="5b60cdee9ee9cbb13f4af0a40abdd177")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-gtable", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-uwot", type=("build", "run"))
    depends_on("r-enrichr", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-mcmcprecision", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-withr", type=("build", "run"))
    depends_on("r-scater@1.14.4:", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-dbscan", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-dendextend", type=("build", "run"))
    depends_on("r-ggdendro", type=("build", "run"))
    depends_on("r-proc", type=("build", "run"))
