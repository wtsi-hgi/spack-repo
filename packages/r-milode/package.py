# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMilode(RPackage):
    """Framework for sensitive DE testing (using neighbourhoods).

    miloDE builds on an existing framework for DA testing called Milo. It
    exploits the notion of overlapping neighborhoods of homogeneous cells,
    constructed from graph-representation of scRNA-seq data, and performs
    testing within each neighborhood. Multiple testing correction is performed
    either across neighborhoods or across genes.

    """
    
    homepage = "https://github.com/MarioniLab/miloDE"
    git = "https://github.com/MarioniLab/miloDE.git"

    version("2024-04-05", commit="3f825b946f21f2b2ccd2331aaf1672ce6615b778")

    depends_on("dplyr", type=("build", "run"))
    depends_on("ggplot2", type=("build", "run"))
    depends_on("ggpubr", type=("build", "run"))
    depends_on("Matrix", type=("build", "run"))
    depends_on("scuttle", type=("build", "run"))
    depends_on("SingleCellExperiment", type=("build", "run"))
    depends_on("SummarizedExperiment", type=("build", "run"))
    depends_on("stats", type=("build", "run"))
    depends_on("tibble", type=("build", "run"))
    depends_on("RcppGreedySetCover", type=("build", "run"))
    depends_on("igraph", type=("build", "run"))
    depends_on("miloR", type=("build", "run"))
    depends_on("edgeR", type=("build", "run")) 
    depends_on("Augur", type=("build", "run"))
    depends_on("S4Vectors", type=("build", "run"))
    depends_on("reshape2", type=("build", "run"))
    depends_on("ggraph", type=("build", "run"))
    depends_on("grDevices", type=("build", "run"))
    depends_on("BiocParallel", type=("build", "run"))
    depends_on("RColorBrewer", type=("build", "run"))
    depends_on("methods", type=("build", "run"))
    depends_on("ggbeeswarm", type=("build", "run"))
    depends_on("limma", type=("build", "run"))