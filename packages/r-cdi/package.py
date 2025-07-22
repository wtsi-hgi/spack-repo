# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdi(RPackage):
    """Clustering Deviation Index (CDI)

    Single-cell RNA-sequencing (scRNA-seq) is widely used to explore cellular variation. The analysis of scRNA-seq data often starts from clustering cells into subpopulations. This initial step has a high impact on downstream analyses, and hence it is important to be accurate. However, there have not been unsupervised metric designed for scRNA-seq to evaluate clustering performance. Hence, we propose clustering deviation index (CDI), an unsupervised metric based on the modeling of scRNA-seq UMI counts to evaluate clustering of cells.
    """

    homepage = "https://github.com/jichunxie/CDI"
    bioc = "CDI"

    version("1.6.0", commit="6c5ec2fe3b44262c9e6f6f54a786069c63e338e8")
    version("1.0.2", commit="38c9ab6ad5b9d015031a43acbd6f05d348441bce")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-seuratobject", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ggsci", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
