# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTscan(RPackage):
    """Tools for Single-Cell Analysis

    Provides methods to perform trajectory analysis based on a minimum spanning tree constructed from cluster centroids. Computes pseudotemporal cell orderings by mapping cells in each cluster (or new cells) to the closest edge in the tree. Uses linear modelling to identify differentially expressed genes along each path through the tree. Several plotting and interactive visualization functions are also implemented.
    """

    bioc = "TSCAN"

    version("1.46.0", commit="8ccc82fda282e0a3e2c86728d46115c1aa929a65")
    version("1.40.1", commit="ba0fff8703a7a0a7d5093efc336af5f0d96c6233")

    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-trajectoryutils", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-fastica", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-combinat", type=("build", "run"))
    depends_on("r-mgcv", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
