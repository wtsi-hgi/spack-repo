# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegionalst(RPackage):
    """Investigating regions of interest and performing cross-regional analysis with spatial transcriptomics data

    This package analyze spatial transcriptomics data through cross-regional analysis. It selects regions of interest (ROIs) and identifys cross-regional cell type-specific differential signals. The ROIs can be selected using automatic algorithm or through manual selection. It facilitates manual selection of ROIs using a shiny application.
    """

    bioc = "RegionalST"

    version("1.6.0", commit="a0c7eb36fbb0c27bba14badf7ccb71801815074f")
    version("1.0.1", commit="2544b3ccac74777ac02652a17a37014af0a923dc")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-scater", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-bayesspace", type=("build", "run"))
    depends_on("r-fgsea", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-toast", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
