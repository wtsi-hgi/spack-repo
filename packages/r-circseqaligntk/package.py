# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircseqaligntk(RPackage):
    """A toolkit for end-to-end analysis of RNA-seq data for circular genomes

    CircSeqAlignTk is designed for end-to-end RNA-Seq data analysis of circular genome sequences, from alignment to visualization. It mainly targets viroids which are composed of 246-401 nt circular RNAs. In addition, CircSeqAlignTk implements a tidy interface to generate synthetic sequencing data that mimic real RNA-Seq data, allowing developers to evaluate the performance of alignment tools and workflows.
    """

    homepage = "https://github.com/jsun/CircSeqAlignTk"
    bioc = "CircSeqAlignTk"

    version("1.10.0", commit="a2168788cc892aca3a5a467972c9da0c57959284")
    version("1.4.0", commit="958204b04d4e70d948f11ed567cb39426f99860e")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-shortread", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-rbowtie2", type=("build", "run"))
    depends_on("r-rhisat2", type=("build", "run"))
    # GUI and utilities required by upstream DESCRIPTION
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinyfiles", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
