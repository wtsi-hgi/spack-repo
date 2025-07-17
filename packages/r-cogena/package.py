# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCogena(RPackage):
    """co-expressed gene-set enrichment analysis

    cogena is a workflow for co-expressed gene-set enrichment analysis. It aims to discovery smaller scale, but highly correlated cellular events that may be of great biological relevance. A novel pipeline for drug discovery and drug repositioning based on the cogena workflow is proposed. Particularly, candidate drugs can be predicted based on the gene expression of disease-related data, or other similar drugs can be identified based on the gene expression of drug-related data. Moreover, the drug mode of action can be disclosed by the associated pathway analysis. In summary, cogena is a flexible workflow for various gene set enrichment analysis for co-expressed genes, with a focus on pathway/GO analysis and drug repositioning.
    """

    homepage = "https://github.com/zhilongjia/cogena"
    bioc = "cogena"

    version("1.42.0", commit="31579055843754373e8913da2d3934337a9cfe03")
    version("1.36.0", commit="6989324d86918dbd0cf4c4891073de84eafd611d")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-kohonen", type=("build", "run"))
    depends_on("r-class", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-amap", type=("build", "run"))
    depends_on("r-apcluster", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-fastcluster", type=("build", "run"))
    depends_on("r-corrplot", type=("build", "run"))
    depends_on("r-biwt", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
