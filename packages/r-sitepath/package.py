# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSitepath(RPackage):
    """Phylogeny-based sequence clustering with site polymorphism

    Using site polymorphism is one of the ways to cluster DNA/protein sequences but it is possible for the sequences with the same polymorphism on a single site to be genetically distant. This package is aimed at clustering sequences using site polymorphism and their corresponding phylogenetic trees. By considering their location on the tree, only the structurally adjacent sequences will be clustered. However, the adjacent sequences may not necessarily have the same polymorphism. So a branch-and-bound like algorithm is used to minimize the entropy representing the purity of site polymorphism of each cluster.
    """

    homepage = "https://wuaipinglab.github.io/sitePath/"
    bioc = "sitePath"

    version("1.24.0", commit="c308da0aafb4453310f696e5b5e033de26949946")
    version("1.18.0", commit="b07adeea85cc7665b877cfee058586d316952fb8")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-aplot", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-ggtree", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-seqinr", type=("build", "run"))
    depends_on("r-tidytree", type=("build", "run"))
