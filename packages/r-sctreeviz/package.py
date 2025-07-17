# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSctreeviz(RPackage):
    """R/Bioconductor package to interactively explore and visualize single cell RNA-seq datasets with hierarhical annotations

    scTreeViz provides classes to support interactive data aggregation and visualization of single cell RNA-seq datasets with hierarchies for e.g. cell clusters at different resolutions. The `TreeIndex` class provides methods to manage hierarchy and split the tree at a given resolution or across resolutions. The `TreeViz` class extends `SummarizedExperiment` and can performs quick aggregations on the count matrix defined by clusters.
    """

    bioc = "scTreeViz"

    version("1.14.1", commit="ef6773dfede869a077731567218c95ea4f964125")
    version("1.8.0", commit="2e0db4d7000ad820249a037f951347fa29c13278")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-epivizr", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-clustree", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-sys", type=("build", "run"))
    depends_on("r-epivizrdata", type=("build", "run"))
    depends_on("r-epivizrserver", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
    depends_on("r-scater", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
