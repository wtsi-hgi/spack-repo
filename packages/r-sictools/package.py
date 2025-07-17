# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSictools(RPackage):
    """Find SNV/Indel differences between two bam files with near relationship

    This package is to find SNV/Indel differences between two bam files with near relationship in a way of pairwise comparison thourgh each base position across the genome region of interest. The difference is inferred by fisher test and euclidean distance, the input of which is the base count (A,T,G,C) in a given position and read counts for indels that span no less than 2bp on both sides of indel region.
    """

    bioc = "SICtools"

    version("1.38.0", commit="20dae93a64e252e3498b2db9a0c90abf79f0bcea")
    version("1.32.0", commit="49e086b4d347b7e875f454e914581fbbb9a50da8")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-rsamtools@1.18.1:", type=("build", "run"))
    depends_on("r-doparallel@1.0.8:", type=("build", "run"))
    depends_on("r-biostrings@2.32.1:", type=("build", "run"))
    depends_on("r-stringr@0.6.2:", type=("build", "run"))
    depends_on("r-matrixstats@0.10:", type=("build", "run"))
    depends_on("r-plyr@1.8.3:", type=("build", "run"))
    depends_on("r-genomicranges@1.22.4:", type=("build", "run"))
    depends_on("r-iranges@2.4.8:", type=("build", "run"))
    depends_on("ncurses", type=("build", "link", "run"))
    depends_on("zlib", type=("build", "link", "run"))

    def patch(self):
        filter_file("-lcurses", "-lcurses -ltinfo", "src/Makefile", string=True)
