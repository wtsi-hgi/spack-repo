# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSracipe(RPackage):
    """Systems biology tool to simulate gene regulatory circuits

    sRACIPE implements a randomization-based method for gene circuit modeling. It allows us to study the effect of both the gene expression noise and the parametric variation on any gene regulatory circuit (GRC) using only its topology, and simulates an ensemble of models with random kinetic parameters at multiple noise levels. Statistical analysis of the generated gene expressions reveals the basin of attraction and stability of various phenotypic states and their changes associated with intrinsic and extrinsic noises. sRACIPE provides a holistic picture to evaluate the effects of both the stochastic nature of cellular processes and the parametric variation.
    """

    homepage = "https://vivekkohar.github.io/sRACIPE/"
    bioc = "sRACIPE"

    version("2.0.1", commit="1c51770636823a262d260e861284a67079bacc4a")
    version("1.18.0", commit="6b8825430c77a388a12cb78badf56304f5c5e62c")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-visnetwork", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-umap", type=("build", "run"))
    depends_on("r-htmlwidgets", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
