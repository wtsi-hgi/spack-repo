# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLintind(RPackage):
    """Lineage tracing by indels

    When we combine gene-editing technology and sequencing technology, we need to reconstruct a lineage tree from alleles generated and calculate the similarity between each pair of groups. FindIndel() and IndelForm() function will help you align each read to reference sequence and generate scar form strings respectively. IndelIdents() function will help you to define a scar form for each cell or read. IndelPlot() function will help you to visualize the distribution of deletion and insertion. TagProcess() function will help you to extract indels for each cell or read. TagDist() function will help you to calculate the similarity between each pair of groups across the indwells they contain. BuildTree() function will help you to reconstruct a tree. PlotTree() function will help you to visualize the tree.
    """

    bioc = "LinTInd"

    version("1.12.0", commit="6f017ede6ad55bf75709d111d3d66d5558efd0d3")
    version("1.6.0", commit="cf761b6c73a965eefac662df46284e5d168926d2")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-data-tree", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-networkd3", type=("build", "run"))
    depends_on("r-stringdist", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-ggnewscale", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-rlist", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biocgenerics@0.36.1:", type=("build", "run"))
    depends_on("r-ggtree", type=("build", "run"))
