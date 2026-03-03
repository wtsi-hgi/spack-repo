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

    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-scuttle", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rcppgreedysetcover", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-milor", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-edger", type=("build", "run")) 
    depends_on("r-augur", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-ggbeeswarm", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))