# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrandcheckr(RPackage):
    """Calculate strandness information of a bam file

    This package aims to quantify and remove putative double strand DNA from a strand-specific RNA sample. There are also options and methods to plot the positive/negative proportions of all sliding windows, which allow users to have an idea of how much the sample was contaminated and the appropriate threshold to be used for filtering.
    """

    homepage = "https://github.com/UofABioinformaticsHub/strandCheckR"
    bioc = "strandCheckR"

    version("1.26.0", commit="17a91b3decb6ae1d4f918abc34d215a14edf08e9")
    version("1.20.0", commit="29e1843f8b9799e844a21e45a808a89631a25458")

    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
