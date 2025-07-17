# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgc(RPackage):
    """A fast hierarchical graph-based clustering method

    HGC (short for Hierarchical Graph-based Clustering) is an R package for conducting hierarchical clustering on large-scale single-cell RNA-seq (scRNA-seq) data. The key idea is to construct a dendrogram of cells on their shared nearest neighbor (SNN) graph. HGC provides functions for building graphs and for conducting hierarchical clustering on the graph. The users with old R version could visit https://github.com/XuegongLab/HGC/tree/HGC4oldRVersion to get HGC package built for R 3.6.
    """

    bioc = "HGC"

    version("1.16.0", commit="3ebd916006f8b1484e7ebc4833edd3e148fc3cd5")
    version("1.10.0", commit="7c4a634754e4e87a94b8b718bfef3f78b4b6adf2")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rann", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-dendextend", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
