# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetascope(RPackage):
    """Tools and functions for preprocessing 16S and metagenomic sequencing microbiome data

    This package contains tools and methods for preprocessing microbiome data. Functionality includes library generation, demultiplexing, alignment, and microbe identification.  It is in part an R translation of the PathoScope 2.0 pipeline.
    """

    homepage = "https://github.com/compbiomed/metascope"
    bioc = "MetaScope"

    version("1.8.1", commit="b713f8c5532787050e9148783bea6ffcbff6722b")
    version("1.2.0", commit="fec11ab09908fa0c3ed4f84e8f626318c008ae28")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-rbowtie2", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-taxize", type=("build", "run"))
    depends_on("r-taxonomizr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-qlcmatrix", type=("build", "run"))
