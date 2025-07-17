# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeandleaf(RPackage):
    """Displaying binary trees with focus on dendrogram leaves

    The TreeAndLeaf package combines unrooted and force-directed graph algorithms in order to layout binary trees, aiming to represent multiple layers of information onto dendrogram leaves.
    """

    bioc = "TreeAndLeaf"

    version("1.20.0", commit="3a797ab3dc7a05552d323228d7349f7d46d9cbec")
    version("1.14.0", commit="f57a9339c970aad701318549b34dd13482da55f0")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-reder@1.40.4:", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
