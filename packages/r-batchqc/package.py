# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchqc(RPackage):
    """Batch Effects Quality Control Software

    Sequencing and microarray samples often are collected or processed in multiple batches or at different times. This often produces technical biases that can lead to incorrect results in the downstream analysis. BatchQC is a software tool that streamlines batch preprocessing and evaluation by providing interactive diagnostics, visualizations, and statistical analyses to explore the extent to which batch variation impacts the data. BatchQC diagnostics help determine whether batch adjustment needs to be done, and how correction should be applied before proceeding with a downstream analysis. Moreover, BatchQC interactively applies multiple common batch effect approaches to the data, and the user can quickly see the benefits of each method. BatchQC is developed as a Shiny App. The output is organized into multiple tabs, and each tab features an important part of the batch effect analysis and visualization of the data. The BatchQC interface has the following analysis groups: Summary, Differential Expression, Median Correlations, Heatmaps, Circular Dendrogram, PCA Analysis, Shape, ComBat and SVA.
    """

    homepage = "https://github.com/mani2012/BatchQC"
    bioc = "BatchQC"

    version("2.4.0", commit="b31f36a4606f852335a0719cc5719b7265e96932")
    version("1.30.0", commit="3ece1d72469cba0552b62ef6074447bc2f6cdac9")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-pander", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-mcmcpack", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
    depends_on("r-corpcor", type=("build", "run"))
    depends_on("r-moments", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-ggvis", type=("build", "run"))
    depends_on("r-heatmaply", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("pandoc", type=("build", "link", "run"))
    # Additional dependencies required by 2.4.0
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-ebseq", type=("build", "run"))
    depends_on("r-ggdendro", type=("build", "run"))
    depends_on("r-ggnewscale", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-reader", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-shinythemes", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tidyverse", type=("build", "run"))
    depends_on("r-umap", type=("build", "run"))
