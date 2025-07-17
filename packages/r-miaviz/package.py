# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiaviz(RPackage):
    """Microbiome Analysis Plotting and Visualization

    The miaViz package implements functions to visualize TreeSummarizedExperiment objects especially in the context of microbiome analysis. Part of the mia family of R/Bioconductor packages.
    """

    bioc = "miaViz"

    version("1.16.0", commit="b1ea3a893e4103141955b1a1c069329398a053ea")
    version("1.10.0", commit="09da1eb2de9c0cafdcb248ec43fa5c99fd341d9f")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-treesummarizedexperiment", type=("build", "run"))
    depends_on("r-mia@0.99:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggraph@2:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-scater", type=("build", "run"))
    depends_on("r-ggtree", type=("build", "run"))
    depends_on("r-ggnewscale", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidytree", type=("build", "run"))
    depends_on("r-tidygraph", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-dirichletmultinomial", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
