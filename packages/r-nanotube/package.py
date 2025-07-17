# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanotube(RPackage):
    """An Easy Pipeline for NanoString nCounter Data Analysis

    NanoTube includes functions for the processing, quality control, analysis, and visualization of NanoString nCounter data. Analysis functions include differential analysis and gene set analysis methods, as well as postprocessing steps to help understand the results. Additional functions are included to enable interoperability with other Bioconductor NanoString data analysis packages.
    """

    bioc = "NanoTube"

    version("1.14.0", commit="9fd718e1163178aceca37a25582b8fe8bbc6d3bf")
    version("1.8.0", commit="61097e411c8951bd2ce57092f8bc534eeb3a400e")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-fgsea", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))
