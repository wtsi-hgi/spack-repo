# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbnplot(RPackage):
    """plot bayesian network inferred from gene expression data based on enrichment analysis results

    This package provides the visualization of bayesian network inferred from gene expression data. The networks are based on enrichment analysis results inferred from packages including clusterProfiler and ReactomePA. The networks between pathways and genes inside the pathways can be inferred and visualized.
    """

    homepage = "https://github.com/noriakis/CBNplot"
    bioc = "CBNplot"

    version("1.8.0", commit="a9f143fc4fe06ef52525ef64384a799c8a7e3be8")
    version("1.2.1", commit="ccccb660046347027bcf447da671f620e759ecad")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-graphite", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-bnlearn@4.7:", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-clusterprofiler", type=("build", "run"))
    depends_on("r-enrichplot", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ggforce", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-depmap", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-rmpfr", type=("build", "run"))
    depends_on("r-graphlayouts", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-ggdist", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-pvclust", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-oaqc", type=("build", "run"))
