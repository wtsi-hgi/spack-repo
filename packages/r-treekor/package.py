# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreekor(RPackage):
    """Cytometry Cluster Hierarchy and Cellular-to-phenotype Associations

    treekoR is a novel framework that aims to utilise the hierarchical nature of single cell cytometry data to find robust and interpretable associations between cell subsets and patient clinical end points. These associations are aimed to recapitulate the nested proportions prevalent in workflows inovlving manual gating, which are often overlooked in workflows using automatic clustering to identify cell populations. We developed treekoR to: Derive a hierarchical tree structure of cell clusters; quantify a cell types as a proportion relative to all cells in a sample (%total), and, as the proportion relative to a parent population (%parent); perform significance testing using the calculated proportions; and provide an interactive html visualisation to help highlight key results.
    """

    bioc = "treekoR"

    version("1.16.0", commit="d8a669af6b77a6041014d12c8d047ef6ec8b16ab")
    version("1.10.0", commit="cd2ce9f536768b277936a8bc92c71975b1ea9554")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggiraph", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-hopach", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-ggtree", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-diffcyt", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-multcomp", type=("build", "run"))
