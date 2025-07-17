# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrisfgm(RPackage):
    """Comprehensive Analysis of Gene Interactivity Networks Based on Single-Cell RNA-Seq

    Single-cell RNA-Seq data is useful in discovering cell heterogeneity and signature genes in specific cell populations in cancer and other complex diseases. Specifically, the investigation of functional gene modules (FGM) can help to understand gene interactive networks and complex biological processes. QUBIC2 is recognized as one of the most efficient and effective tools for FGM identification from scRNA-Seq data. However, its availability is limited to a C implementation, and its applicative power is affected by only a few downstream analyses functionalities. We developed an R package named IRIS-FGM (integrative scRNA-Seq interpretation system for functional gene module analysis) to support the investigation of FGMs and cell clustering using scRNA-Seq data. Empowered by QUBIC2, IRIS-FGM can identify co-expressed and co-regulated FGMs, predict types/clusters, identify differentially expressed genes, and perform functional enrichment analysis. It is noteworthy that IRIS-FGM also applies Seurat objects that can be easily used in the Seurat vignettes.
    """

    bioc = "IRISFGM"

    version("1.10.0", commit="27aef48d0fc2d339236e0e2413402116a997e39b")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-mcl", type=("build", "run"))
    depends_on("r-anocva", type=("build", "run"))
    depends_on("r-polychrome", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-org-mm-eg-db", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-adaptgauss", type=("build", "run"))
    depends_on("r-desingle", type=("build", "run"))
    depends_on("r-drimpute", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-clusterprofiler", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-mixtools", type=("build", "run"))
    depends_on("r-scater", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
