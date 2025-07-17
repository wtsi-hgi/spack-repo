# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMineica(RPackage):
    """Analysis of an ICA decomposition obtained on genomics data

    The goal of MineICA is to perform Independent Component Analysis (ICA) on multiple transcriptome datasets, integrating additional data (e.g molecular, clinical and pathological). This Integrative ICA helps the biological interpretation of the components by studying their association with variables (e.g sample annotations) and gene sets, and enables the comparison of components from different datasets using correlation-based graph.
    """

    bioc = "MineICA"

    version("1.48.0", commit="4c7d2f72c9dc34793d5d0e670a35ff6ce818fe6b")
    version("1.42.0", commit="c4e24ac906b42aa4796933cc364dfdf6c17cb050")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biocgenerics@0.13.8:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-xtable", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-gostats", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-marray", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-annotate", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-fastica", type=("build", "run"))
    depends_on("r-jade", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-lumi", type=("build", "run"))
    depends_on("r-fpc", type=("build", "run"))
    depends_on("r-lumihumanall-db", type=("build", "run"))
