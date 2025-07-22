# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMitch(RPackage):
    """Multi-Contrast Gene Set Enrichment Analysis

    mitch is an R package for multi-contrast enrichment analysis. At it’s heart, it uses a rank-MANOVA based statistical approach to detect sets of genes that exhibit enrichment in the multidimensional space as compared to the background. The rank-MANOVA concept dates to work by Cox and Mann (https://doi.org/10.1186/1471-2105-13-S16-S12). mitch is useful for pathway analysis of profiling studies with one, two or more contrasts, or in studies with multiple omics profiling, for example proteomic, transcriptomic, epigenomic analysis of the same samples. mitch is perfectly suited for pathway level differential analysis of scRNA-seq data. The main strengths of mitch are that it can import datasets easily from many upstream tools and has advanced plotting features to visualise these enrichments.
    """

    homepage = "https://github.com/markziemann/mitch"
    bioc = "mitch"

    version("1.14.0", commit="2f0452fc5b2d503e24dfd0e87474060526ec619b")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ggally", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-beeswarm", type=("build", "run"))
    depends_on("r-echarts4r", type=("build", "run"))
    depends_on("r-kableextra", type=("build", "run"))
