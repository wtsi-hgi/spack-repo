# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSarks(RPackage):
    """Suffix Array Kernel Smoothing for discovery of correlative sequence motifs and multi-motif domains

    Suffix Array Kernel Smoothing (see https://academic.oup.com/bioinformatics/article-abstract/35/20/3944/5418797), or SArKS, identifies sequence motifs whose presence correlates with numeric scores (such as differential expression statistics) assigned to the sequences (such as gene promoters). SArKS smooths over sequence similarity, quantified by location within a suffix array based on the full set of input sequences. A second round of smoothing over spatial proximity within sequences reveals multi-motif domains. Discovered motifs can then be merged or extended based on adjacency within MMDs. False positive rates are estimated and controlled by permutation testing.
    """

    homepage = (
        "https://academic.oup.com/bioinformatics/article-abstract/35/20/3944/5418797"
    )
    bioc = "sarks"

    version("1.20.0", commit="af5b861b8c61b25c51ca9abb1bb4b6fd8b7e33e1")
    version("1.14.0", commit="acd4c7f2dc8266507428814f4c3a3f1198d6a816")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-rjava", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-binom", type=("build", "run"))
    depends_on("openjdk@1.8:", type=("build", "link", "run"))
