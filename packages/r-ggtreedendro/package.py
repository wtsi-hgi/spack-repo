# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtreedendro(RPackage):
    """Drawing 'dendrogram' using 'ggtree'

    Offers a set of 'autoplot' methods to visualize tree-like structures (e.g., hierarchical clustering and classification/regression trees) using 'ggtree'. You can adjust graphical parameters using grammar of graphic syntax and integrate external data to the tree.
    """

    bioc = "ggtreeDendro"

    version("1.10.0", commit="aac65c04319be43d5b5c3c83c40f0cfec417d3f6")
    version("1.4.0", commit="32d96cd6f0924d4a786b035eddc9a9ef914ce7bd")

    depends_on("r-ggtree@3.5.3:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-tidytree", type=("build", "run"))
