# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeurat(RPackage):
    """Tools for Single Cell Genomics.

    A toolkit for quality control, analysis, and exploration of single cell RNA
    sequencing data. 'Seurat' aims to enable users to identify and interpret
    sources of heterogeneity from single cell transcriptomic measurements, and
    to integrate diverse types of single cell data. See Satija R, Farrell J,
    Gennert D, et al (2015) <doi:10.1038/nbt.3192>, Macosko E, Basu A, Satija
    R, et al (2015) <doi:10.1016/j.cell.2015.05.002>, and Stuart T, Butler A,
    et al (2019) <doi:10.1016/j.cell.2019.05.031> for more details."""

    # cran = "Seurat"
    git = "https://github.com/satijalab/seurat"

    version("4.9.9", branch="seurat5")
    version("4.2.1", sha256="410238b6ca147451b43800a6e49c132fa5f6aacfe6b93b39a1e4d61257a9e35e")
    version("4.2.0", sha256="22a3d22a9ba255c4db5b37339b183fdfb91e2d37a8b8d58a9ff45b1bc414ebef")
    version("4.1.1", sha256="201aa96919b32378fc4cb67557188214c1242dcbae50cadd7d12c86666af8ace")
    version("4.1.0", sha256="2505829a2763e449684dd1b107ee6982e019ee9fecb093adca7b283cad1b315d")
    version("3.2.3", sha256="83aa48f75c3756bee23e108a8b01028366e24f237fe990cb441f3525e0613f87")
    version("3.1.0", sha256="d8d3fad2950a8f791376e3d20c72ea07c68bf8d82d800661cab5ce696db39d45")
    version("3.0.2", sha256="16df5dec6b41d49320c5bf5ce30eb3b7dedeea69b054b55b77528f2f2b7bce04")
    version("3.0.1", sha256="8c467bdbfdb9aff51bde6a897ff98a7389941f688639d8f1d36c71dde076a257")
    version("2.1.0", sha256="7d20d231b979a4aa63cd7dae7e725405212e8975889f12b8d779c6c896c10ac3")
    version("2.0.1", sha256="6aa33aa3afb29a8be364ab083c7071cfbc56ad042a019bcf6f939e0c8c7744f0")

    depends_on("r@3.2.0:", type=("build", "run"))
    depends_on("r@3.4.0:", type=("build", "run"), when="@2.3.1:")
    depends_on("r@3.6.0:", type=("build", "run"), when="@3.2.3:")
    depends_on("r@4.0.0:", type=("build", "run"), when="@4.1.0:")
    depends_on("r-cluster", type=("build", "run"), when="@2.3.0:")
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-fitdistrplus", type=("build", "run"), when="@2.3.0:")
    depends_on("r-future", type=("build", "run"), when="@3.0.0:")
    depends_on("r-future-apply", type=("build", "run"), when="@3.0.0:")
    depends_on("r-ggplot2@3.0.0:", type=("build", "run"))
    depends_on("r-ggplot2@3.3.0:", type=("build", "run"), when="@3.2.3:")
    depends_on("r-ggrepel", type=("build", "run"), when="@3.0.0:")
    depends_on("r-ggridges", type=("build", "run"), when="@2.2.0:")
    depends_on("r-httr", type=("build", "run"), when="@2.3.4:")
    depends_on("r-ica", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-irlba", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"), when="@3.2.3:")
    depends_on("r-kernsmooth", type=("build", "run"), when="@3.0.0:")
    depends_on("r-leiden@0.3.1:", type=("build", "run"), when="@3.1.0:")
    depends_on("r-lmtest", type=("build", "run"), when="@2.3.0:")
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-matrix@1.2-14:", type=("build", "run"))
    depends_on("r-matrix@1.5-0", type=("build", "run"), when="@4.2.0:")
    depends_on("r-matrixstats", type=("build", "run"), when="@3.2.3:")
    depends_on("r-miniui", type=("build", "run"), when="@3.2.3:")
    depends_on("r-patchwork", type=("build", "run"), when="@3.2.3:")
    depends_on("r-pbapply", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-plotly@4.9.0:", type=("build", "run"), when="@3.2.3:")
    depends_on("r-png", type=("build", "run"), when="@2.3.0:")
    depends_on("r-rann", type=("build", "run"), when="@2.3.0:")
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rcpp@0.11.0:", type=("build", "run"))
    depends_on("r-rcpp@1.0.7:", type=("build", "run"), when="@4.1.0:")
    depends_on("r-rcppannoy", type=("build", "run"), when="@3.1.0:")
    depends_on("r-rcppannoy@0.0.18:", type=("build", "run"), when="@4.1.0:")
    depends_on("r-reticulate", type=("build", "run"), when="@2.3.1:")
    depends_on("r-rlang", type=("build", "run"), when="@3.0.0:")
    depends_on("r-rocr", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"), when="@3.0.0:")
    depends_on("r-scattermore@0.7:", type=("build", "run"), when="@3.2.3:")
    depends_on("r-sctransform@0.2.0:", type=("build", "run"), when="@3.0.0:")
    depends_on("r-sctransform@0.3.1:", type=("build", "run"), when="@3.2.3:")
    depends_on("r-sctransform@0.3.3:", type=("build", "run"), when="@4.1.0:")
    depends_on("r-sctransform@0.3.4:", type=("build", "run"), when="@4.2.0:")
    depends_on("r-sctransform@0.3.5:", type=("build", "run"), when="@4.2.1:")
    depends_on("r-seuratobject@4.0.4:", type=("build", "run"), when="@4.1.0:")
    depends_on("r-seuratobject@4.1.0:", type=("build", "run"), when="@4.1.1:")
    depends_on("r-seuratobject@4.1.2:", type=("build", "run"), when="@4.2.0:")
    depends_on("r-seuratobject@4.1.3:", type=("build", "run"), when="@4.2.1:")
    depends_on("r-seuratobject@4.9.9", type=("build", "run"), when="@4.9.9:")
    depends_on("r-bpcells", type=("build", "run"), when="@4.9.9:")
    depends_on("r-shiny", type=("build", "run"), when="@3.2.3:")
    depends_on("r-spatstat-explore", type=("build", "run"), when="@4.2.1:")
    depends_on("r-spatstat-geom", type=("build", "run"), when="@4.1.0:")
    depends_on("r-tibble", type=("build", "run"), when="@3.2.3:")
    depends_on("r-uwot", type=("build", "run"), when="@3.1.0:")
    depends_on("r-uwot@0.1.9:", type=("build", "run"), when="@3.2.3:")
    depends_on("r-uwot@0.1.14:", type=("build", "run"), when="@4.2.0:")
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-rcppprogress", type=("build", "run"))

    depends_on("r-gplots", type=("build", "run"), when="@:2.3.4")
    depends_on("r-reshape2", type=("build", "run"), when="@:2.3.4")
    depends_on("r-ape", type=("build", "run"), when="@:3.1.0")
    depends_on("r-tidyr", type=("build", "run"), when="@:2.3.4")
    depends_on("r-caret", type=("build", "run"), when="@:2.3.2")
    depends_on("r-gdata", type=("build", "run"), when="@:2.3.2")
    depends_on("r-gridextra", type=("build", "run"), when="@:2.3.0")
    depends_on("r-hmisc", type=("build", "run"), when="@:2.3.4")
    depends_on("r-nmf", type=("build", "run"), when="@:2.2.0")
    depends_on("r-fpc", type=("build", "run"), when="@:2.3.4")
    depends_on("r-lars", type=("build", "run"), when="@:2.3.4")
    depends_on("r-dtw", type=("build", "run"), when="@:2.3.4")
    depends_on("r-mixtools", type=("build", "run"), when="@:2.3.4")
    depends_on("r-diffusionmap", type=("build", "run"), when="@:2.3.3")
    depends_on("r-tsne", type=("build", "run"), when="@:3.1.0")
    depends_on("r-ranger", type=("build", "run"), when="@:2.3.2")
    depends_on("r-ggjoy", type=("build", "run"), when="@:2.1.0")
    depends_on("r-sdmtools", type=("build", "run"), when="@:3.1.0")
    depends_on("r-tclust", type=("build", "run"), when="@:2.3.2")
    depends_on("r-fnn", type=("build", "run"), when="@:2.3.2")
    depends_on("r-vgam", type=("build", "run"), when="@:2.3.2")
    depends_on("r-e1071", type=("build", "run"), when="@:2.0.1")
    depends_on("r-compositions", type=("build", "run"), when="@:2.0.1")
    depends_on("r-nmof", type=("build", "run"), when="@:2.0.1")
    depends_on("r-metap", type=("build", "run"), when="@2.2.1:3.1.0")
    depends_on("r-stringr", type=("build", "run"), when="@:2.3.2")
    depends_on("r-dplyr", type=("build", "run"), when="@:2.3.4")
    depends_on("r-dosnow", type=("build", "run"), when="@2.3.0:2.3.4")
    depends_on("r-foreach", type=("build", "run"), when="@2.3.0:2.3.4")
    depends_on("r-hdf5r", type=("build", "run"), when="@2.3.2:2.3.4")
    depends_on("r-rsvd", type=("build", "run"), when="@3.0.0:3.2.3")
    depends_on("r-spatstat@:1.64-1", type=("build", "run"), when="@3.2.3")
    depends_on("java", when="@:2.3.0")
    depends_on("r-spatstat-core", type=("build", "run"), when="@4.1.0:")
    depends_on("r-spatstat-core", when="@:4.2.0")
    depends_on("r-rcpp-hnsw", when="@4.9.9:")
    depends_on("r-fast-dummies", when="@4.9.9:")
