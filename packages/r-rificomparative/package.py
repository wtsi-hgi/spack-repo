# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRificomparative(RPackage):
    """'rifiComparative' compares the output of rifi from two different conditions.

    'rifiComparative' is a continuation of rifi package. It compares two conditions output of rifi using half-life and mRNA at time 0 segments. As an input for the segmentation, the difference between half-life of both condtions and log2FC of the mRNA at time 0 are used. The package provides segmentation, statistics, summary table, fragments visualization and some additional useful plots for further anaylsis.
    """

    bioc = "rifiComparative"

    version("1.8.0", commit="9976f28e2d9d22dae621c5534b6832b6a66b0855")
    version("1.2.0", commit="a1ac42baf035c719a4b5e4639f88997336974575")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-domc", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-egg", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-nnet", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-writexl", type=("build", "run"))
    depends_on("r-dta", type=("build", "run"))
    depends_on("r-lsd", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
