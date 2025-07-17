# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglecellsignalr(RPackage):
    """Cell Signalling Using Single Cell RNAseq Data Analysis

    Allows single cell RNA seq data analysis, clustering, creates internal network and infers cell-cell interactions.
    """

    bioc = "SingleCellSignalR"

    version("1.20.0", commit="2e7e46d23284657f8edb923c26ab41cef40a7e2d")
    version("1.14.0", commit="cd135991d3d8700204440bcedcc3e41d08542bfc")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-multtest", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
