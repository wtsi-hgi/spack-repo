# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApl(RPackage):
    """Association Plots

    APL is a package developed for computation of Association Plots (AP), a method for visualization and analysis of single cell transcriptomics data. The main focus of APL is the identification of genes characteristic for individual clusters of cells from input data. The package performs correspondence analysis (CA) and allows to identify cluster-specific genes using Association Plots. Additionally, APL computes the cluster-specificity scores for all genes which allows to rank the genes by their specificity for a selected cell cluster of interest.
    """

    homepage = "https://vingronlab.github.io/APL/"
    bioc = "APL"

    version("1.12.0", commit="15423f6254a470dafdceba84f9e594541d8540bf")
    version("1.6.1", commit="56ef8fbd54c7a63f167fb04a2ac465d40d1f9fb1")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-viridislite", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-topgo", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-org-mm-eg-db", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("python", type=("build", "link", "run"))
    depends_on("py-torch", type=("build", "link", "run"))
    depends_on("py-numpy", type=("build", "link", "run"))
    depends_on("r@4.4.0:", when="@1.12.0:", type=("build", "run"))
