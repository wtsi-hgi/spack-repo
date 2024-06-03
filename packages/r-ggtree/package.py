# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtree(RPackage):
    """an R package for visualization of tree and annotation data.

    'ggtree' extends the 'ggplot2' plotting system which implemented the
    grammar of graphics. 'ggtree' is designed for visualization and annotation
    of phylogenetic trees and other tree-like structures with their annotation
    data."""

    bioc = "ggtree"
    urls = [
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ggtree_3.10.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ggtree/ggtree_3.10.1.tar.gz",
    ]
    version("3.8.0", commit="e7c989085d0848e4d5f82aa8000422c71458a9a8")
    version("3.6.2", commit="431ec37bc0f0159b08a7990ce1d9374e160b9f44")
    version("3.4.4", commit="8e48d3e2ea445b6c2213f0471462108a7a72b333")
    version("3.4.0", commit="23f08a3da1829d1bbb6827ed1c4cf878daa4b539")
    version("3.2.1", commit="d3747e636fe1a6a9e09b56a3a3899208ebd05547")
    version("3.10.1", md5="14911b3009b957dcf17ae513e87825fa")
    version("3.10.0", md5="7e1894ce01245d811286b0ce1fbe8266")

    patch("rect_to_poly.patch", when="@3.6.2")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-aplot", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-ggfun@0.0.9:", type=("build", "run"))
    depends_on("r-yulab-utils", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tidytree@0.4.5:", type=("build", "run"))
    depends_on("r-treeio@1.8:", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
