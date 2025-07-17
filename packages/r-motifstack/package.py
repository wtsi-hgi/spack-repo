# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotifstack(RPackage):
    """Plot stacked logos for single or multiple DNA, RNA and amino acid sequence

    The motifStack package is designed for graphic representation of multiple motifs with different similarity scores. It works with both DNA/RNA sequence motif and amino acid sequence motif. In addition, it provides the flexibility for users to customize the graphic parameters such as the font type and symbol colors.
    """

    bioc = "motifStack"

    version("1.52.0", commit="6cf9408c491d1083704f7f249ae6fa2ef2f2a7fb")
    version("1.46.0", commit="80200b0fabeb62db10ea20ea167d8ad2a53ef4db")

    depends_on("r@2.15.1:", type=("build", "run"))
    depends_on("r-ade4", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-htmlwidgets", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-tfbstools", type=("build", "run"))
