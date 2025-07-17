# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMuscat(RPackage):
    """Multi-sample multi-group scRNA-seq data analysis tools

    `muscat` provides various methods and visualization tools for DS analysis in multi-sample, multi-group, multi-(cell-)subpopulation scRNA-seq data, including cell-level mixed models and methods based on aggregated “pseudobulk” data, as well as a flexible simulation platform that mimics both single and multi-sample scRNA-seq data.
    """

    homepage = "https://github.com/HelenaLC/muscat"
    bioc = "muscat"

    version("1.22.0", commit="2d15314e5f661942800560c5582e745f099ea76f")
    version("1.16.0", commit="448b1e846fb5f4e14138293ccc9426e077ba3ca9")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-blme", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-glmmtmb", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-lmertest", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-scater", type=("build", "run"))
    depends_on("r-scuttle", type=("build", "run"))
    depends_on("r-sctransform", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-variancepartition", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
