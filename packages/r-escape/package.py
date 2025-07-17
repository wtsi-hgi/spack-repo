# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REscape(RPackage):
    """Easy single cell analysis platform for enrichment

    A bridging R package to facilitate gene set enrichment analysis (GSEA) in the context of single-cell RNA sequencing. Using raw count information, Seurat objects, or SingleCellExperiment format, users can perform and visualize GSEA across individual cells.
    """

    bioc = "escape"

    version("2.4.0", commit="bc8a5af18b63f47739d9abea5e79f379df8e5ede")
    version("1.12.0", commit="51adca6cb0e3144ca415e5e49212f6a2181accfb")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-gsva", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-ggridges", type=("build", "run"))
    depends_on("r-msigdbr", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-ucell", type=("build", "run"))
    depends_on("r-broom", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
