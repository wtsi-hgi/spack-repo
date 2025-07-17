# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQckitfastq(RPackage):
    """FASTQ Quality Control

    Assessment of FASTQ file format with multiple metrics including quality score, sequence content, overrepresented sequence and Kmers.
    """

    bioc = "qckitfastq"

    version("1.24.0", commit="c160df29fc8b29ff6a6ab04dc858c6a5b3e9c6c1")
    version("1.18.0", commit="ac8f01862d69588fd6e25d2b6aa74ce9f4215253")

    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-seqtools", type=("build", "run"))
    depends_on("r-zlibbioc", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rseqan", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
